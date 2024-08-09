from django.http import JsonResponse
from django.conf import settings

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply API key check for specific paths
        if request.path == '/coredination/get-job-data/':
            api_key = request.headers.get('STVN-API-Key')
            if api_key != settings.STVN_API_KEY:
                return JsonResponse({'error': 'Unauthorized'}, status=401)
        
        return self.get_response(request)
