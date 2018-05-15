from django.http.multipartparser import MultiPartParser
from Api.utils import json_response


def require_login(func):
    """
    # 用户必须登录
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return json_response({
                'state': 401,
                'msg': 'require log in'
            })
        else:
            return func(request, *args, **kwargs)
    return wrapper
