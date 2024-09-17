from django.http import JsonResponse
from django.conf import settings

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/coredination/get-job-data/':
            api_key = request.headers.get('STVN-API-Key')

            settings_api= settings.STVN_API_KEY

            if api_key != settings_api:
                return self.get_response(request)   
        
        return self.get_response(request)
