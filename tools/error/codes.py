from . import APIException

class Success(APIException):
    code = 200
    msg = ""
    status_code = 2000
    data = ""


class Error(APIException):
    code = 200
    msg = ""
    status_code = 5000
    data = ""