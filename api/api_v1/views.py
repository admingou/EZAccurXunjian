from flask import request
from . import api
from EZAccur_xunjian_server.tools.error.codes import Success, Error
from EZAccur_xunjian_server.tools.ReadConfig import ReadConf


@api.route("/test", methods=["GET"])
def  index_api():
    if request.method == "GET":
        return Success(msg="测试数据", data={"name":"gousl","age":24,"project": "go开发工程师"})



@api.route("/loadyaml", methods=["GET"])
def test_getyaml():
    if request.method == "GET":
        conf = ReadConf()
        conf.LoadConf()
        return Success(msg="获取yaml配置", data=conf.GetConf())