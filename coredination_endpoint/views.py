from django.conf import settings
from django.http import JsonResponse
from django.views import View
import requests

class GetJobDataView(View):
    def get(self, request):
        # Get the STVN API key from the request headers
        coredinationAPI_auth = request.headers.get('STVN-API-Key')

        # Compare it with the API key from the settings
        if coredinationAPI_auth != settings.STVN_API_KEY:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        # Make the request to the Coredination API
        url = 'https://app.coredination.net/api/1/job'

        headers = {
            'API-Key': settings.COREDINATION_API_KEY
        }

        try:
            # Request data from the Coredination API
            response = requests.get(url, headers=headers)

            # If the request was successful, return the data
            if response.status_code == 200:
                jobs_data = response.json()
                return JsonResponse(jobs_data, safe=False)
            else:
                return JsonResponse({
                    'error': 'Failed to retrieve data from API',
                    'status_code': response.status_code
                }, status=response.status_code)

        # Handle any request exceptions
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
