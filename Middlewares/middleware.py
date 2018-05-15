from django.utils.deprecation import MiddlewareMixin
from django.http.multipartparser import MultiPartParser


class CommonMiddleware(MiddlewareMixin):
    def process_request(self, request,):
        pass

    def process_response(self, request, response):
        pass


class MethodConvertMiddleware(MiddlewareMixin):
    def process_request(self, request):
        method = request.method
        if method in ['PUT', 'DELETE', 'HEAD', 'OPTIONS']:
            POST, FILES = MultiPartParser(
                request.META, request, request.upload_handlers).parse()
            setattr(request, method.upper(), POST)
            setattr(request, 'FILES', FILES)
