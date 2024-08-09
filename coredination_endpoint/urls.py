from django.urls import path
from django.http import JsonResponse
from .views import GetJobDataView


urlpatterns = [
    path('get-job-data/', GetJobDataView.as_view(), name='get_job_data'),  # This URL requires an API key
]
