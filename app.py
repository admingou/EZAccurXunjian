from flask import Flask
from flask_cors import *
from EZAccur_xunjian_server.api.api_v1 import api
from EZAccur_xunjian_server.tools.error.isweb import is_web_or_api
from EZAccur_xunjian_server.tools.error.web_error import web_errors
from EZAccur_xunjian_server.tools.error import APIException
from werkzeug.exceptions import HTTPException


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