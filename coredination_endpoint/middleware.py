from django.http import JsonResponse
from django.conf import settings

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the path matches, check the API key in the headers
        if request.path == '/coredination/get-job-data/':
            api_key = request.headers.get('STVN-API-Key')

            # Compare it with the correct API key from settings
            if api_key != settings.STVN_API_KEY:
                return JsonResponse({'error': 'Unauthorized'}, status=401)
        
        # Allow the request to continue
        return self.get_response(request)
