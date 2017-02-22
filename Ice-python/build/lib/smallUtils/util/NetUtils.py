from django.http import HttpResponse
import json

class NetUtils:
    def __init__(self):
        return

    def response_success_json(self, content, extra):
        return_info = {'res': 200, 'msg': 'success', 'extra': extra, 'content': json.dumps(content)}
        return HttpResponse(json.dumps(return_info), content_type='application/json')

    def response_fail_json(self, error, extra,code=201):
        return_info = {'res': code, 'msg': str(error), 'extra': extra, 'content': ''}
        return HttpResponse(json.dumps(return_info), content_type='application/json')


class AppException(Exception):
    def __init__(self,err='error',code=201):
        self.message=err
        self.code=code
        Exception.__init__(self,err,code)

