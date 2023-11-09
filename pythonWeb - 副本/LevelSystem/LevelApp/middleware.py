# myapp/middleware.py
from django.http import JsonResponse
from loguru import logger

class MyCustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        error_message = str(exception)  # 将异常信息转换为字符串

        logger.info(f'出现全局异常{error_message}')
        return JsonResponse({'data': f'出现全局异常{error_message}', 'code': 500}, status=500)
