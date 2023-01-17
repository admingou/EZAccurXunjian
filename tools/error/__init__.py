from werkzeug.exceptions import HTTPException
from  flask  import   request,json


class  APIException(HTTPException):
    code = 500
    msg = "服务端开小差了,请联系管理员！"
    status_code = 9999
    data = ""


    def  __init__(self, status_code=None, msg=None, code=None, data=None):
        if code:
            self.code = code
        if status_code:
            self.status_code = status_code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        super(APIException,self).__init__(msg,None)


    def  get_body(self,environ=None):
        body = dict(
            msg = self.msg,
            data = self.data,
            status_code = self.status_code,
            request = request.method + " " + self.get_url_no_param()
        )
        return json.dumps(body, ensure_ascii=False, indent=2).encode("utf-8")



    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]

    @staticmethod
    def  get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return  main_path[0]