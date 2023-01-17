from flask import request
from . import api
from EZAccur_xunjian_server.tools.error.codes import Success, Error


@api.route("/test", methods=["GET"])
def  index_api():
    if request.method == "GET":
        return Success(msg="测试数据", data={"name":"gousl","age":24,"project": "go开发工程师"})