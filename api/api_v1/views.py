from flask import request,current_app
from . import api
from EZAccur_xunjian_server.tools.error.codes import Success, Error
from EZAccur_xunjian_server.tools.ReadConfig import ReadConf


@api.route("/loadyaml", methods=["GET"])
def test_getyaml():
    if request.method == "GET":
        conf = ReadConf()
        conf.LoadConf()
        current_app.logger.info("获取yaml配置成功")
        return Success(msg="获取yaml配置", data=conf.GetConf())