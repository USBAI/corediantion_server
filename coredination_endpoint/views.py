from django.conf import settings
from django.http import JsonResponse
from django.views import View
import requests

class GetJobDataView(View):
    def get(self, request):
        # Retrieve the API key from the request headers
        coredinationAPI_auth = request.headers.get('STVN-API-Key')

        # Check if the provided API key matches the expected key
        if coredinationAPI_auth != settings.STVN_API_KEY:
            # If the API key is invalid, return a 401 Unauthorized response
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        # API endpoint for getting jobs
        url = 'https://app.coredination.net/api/1/job'

        # Set up the headers with the API key for the external request
        headers = {
            'API-Key': settings.COREDINATION_API_KEY  # Ensure this key is set in your Django settings
        }

        try:
            # Send a GET request to the API to retrieve the jobs data
            response = requests.get(url, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the response as JSON
                jobs_data = response.json()
                return JsonResponse(jobs_data, safe=False)
            else:
                # Return an error response if the API call was unsuccessful
                return JsonResponse({
                    'error': 'Failed to retrieve data from API',
                    'status_code': response.status_code
                }, status=response.status_code)
        except requests.exceptions.RequestException as e:
            # Handle exceptions that occur during the API request
            return JsonResponse({'error': str(e)}, status=500)
