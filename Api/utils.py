import json
import uuid

from django.http.response import HttpResponse


def create_uuid():
    return uuid.uuid1().hex


def json_response(data):
    try:
        json_data = json.dumps(data)
    except Exception:
        json_data = json.dumps({})
    return HttpResponse(json_data, content_type='application/json')


def method_not_allowed():
    return HttpResponse(json.dumps({
        'state': 405,
        'msg': 'method not allowed'
    }))


def params_error(errors):
    return HttpResponse(json.dumps({
        'state': 422,
        'msg': '参数错误',
        'data': errors
    }))
