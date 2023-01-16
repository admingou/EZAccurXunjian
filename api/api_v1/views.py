from flask import request
from . import api


def  index_api():
    if request.method == "GET":
        return