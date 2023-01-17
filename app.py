from flask import Flask
from flask_cors import *
from EZAccur_xunjian_server.api.api_v1 import api
from EZAccur_xunjian_server.tools.error.isweb import is_web_or_api
from EZAccur_xunjian_server.tools.error.web_error import web_errors
from EZAccur_xunjian_server.tools.error import APIException
from werkzeug.exceptions import HTTPException
from logging.config import dictConfig
import os


if  not os.path.exists("./logs/"):
    os.mkdir("./logs/")


dictConfig({
        "version": 1,
        "disable_existing_loggers": False,  # 不覆盖默认配置
        "formatters": {  # 日志输出样式
            "default": {
                "format": "%(asctime)s-%(name)s-%(levelname)s-%(message)s"
            }
        },
        "handlers": {
            "log_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "default",   # 日志输出样式对应formatters
                "filename": "./logs/xunjian-info.log",  # 指定log文件目录
                "maxBytes": 20*1024*1024,   # 文件最大20M
                "backupCount": 1000,          # 最多10个文件
                "encoding": "utf8",         # 文件编码
            },

        },
        "root": {
            "level": "INFO",  # # handler中的level会覆盖掉这里的level
            "handlers": ["log_file"],
        },
    }
)


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(api, url_prefix="/api/v1")
# app.config.from_object(config)

@app.errorhandler(Exception)
def  framework_error(e):
    """
    拦截未知异常问题
    异常种类:APIException,
    HTTPException,
    Exception
    :param e:
    :return:
    """
    app.logger.debug(e)
    if is_web_or_api():
        if    isinstance(e,APIException):
              return  e
        if    isinstance(e,HTTPException):
            code = e.code
            msg = e.description
            status_code = 404
            return  APIException(status_code,msg,code)
        else:
            if  not  app.config["DEBUG"]:
                return APIException()
            else:
                raise e
    else:
        return web_errors()



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=7777,debug=False)