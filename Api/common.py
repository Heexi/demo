import json
import time
import os
import random

from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from Api.utils import (json_response, create_uuid,
                       method_not_allowed, params_error)
from Api.decoretors import require_login


def regist_code(request):
    regist_code = random.randint(10000, 10000)
    request.session['regist_code'] = regist_code
    return json_response({
        'state': 200,
        'msg': '获取验证码成功',
        'data': {
            'regist_code': regist_code
        }
    })


@require_login
def user(request):
    method = request.method
    if method == 'GET':
        # 获取用户信息
        return json_response({})
    elif method == 'POST':
        # 更新用户信息
        return json_response({})
    elif method == 'PUT':
        # 注册用户
        data = request.PUT
        username = data.get('username', '')
        password = data.get('password', '')
        ensure_password = data.get('ensure_password', '')
        regist_code = data.get('regist_code', '')
        session_regist_code = request.session.get('regist_code', False)

        errors = dict()
        if User.objects.filter(username=username):
            errors['username'] = '用户名已存在'
        if password < 6:
            errors['password'] = '密码长度不可低于6位'
        if password != ensure_password:
            errors['ensure_password'] = '密码不匹配'
        if regist_code != session_regist_code:
            errors['ensure_password'] = '注册码不匹配'
        if errors:
            return params_error(errors)

        user = User.objects.create(username=username, password=password)
        user.save()
        login(request, user)
        return json_response({
            'state': 200,
            'msg': '参数不正确',
            'data': {'id': user.id}
        })
    else:
        return method_not_allowed()


def session(request):
    method = request.method
    if method == 'GET':
        if request.user.is_authenticated:
            return json_response({
                'state': 200,
                'msg': 'has login'
            })
        return json_response({
            'state': 401,
            'msg': 'did not login'
        })
    elif method == 'PUT':
        data = request.POST
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            data = {
                'state': 200,
                'msg': 'login success'
            }
        else:
            data = {
                'state': 403,
                'msg': '用户名或密码错误'
            }
        return json_response(data)
    elif method == 'DELETE':
        logout(request)
        return json_response({
            'state': 200,
            'msg': 'logout success'
        })
    else:
        return json_response({
            'state': 403,
            'msg': 'method not allowed'
        })
