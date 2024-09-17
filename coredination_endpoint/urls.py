from django.urls import path
from .views import GetJobDataView

urlpatterns = [
    path('get-job-data/', GetJobDataView.as_view(), name='get_job_data'),
]
