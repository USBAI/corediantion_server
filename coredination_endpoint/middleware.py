# middleware.py
from django.http import JsonResponse
from django.conf import settings

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('API-Key')

        # Compare the provided API key with the one in settings
        if api_key != settings.COREDINATION_API_KEY:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response
