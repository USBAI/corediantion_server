# views.py
import requests
from django.http import JsonResponse
from django.views import View

class GetJobDataView(View):
    def get(self, request):
        # Replace these with your actual API key and secret
        api_key = 'd561d1ea-d51f-4b3e-a48a-b5cbf683a732'
        secret_key = 'cec5b414-860b-4298-8cc8-8be849491cbd'

        # API endpoint for getting jobs
        url = 'https://app.coredination.net/api/1/job'

        # Set up the headers with the API key
        headers = {
            'API-Key': api_key
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
                return JsonResponse({'error': 'Failed to retrieve data from API', 'status_code': response.status_code}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            # Handle exceptions that occur during the API request
            return JsonResponse({'error': str(e)}, status=500)
