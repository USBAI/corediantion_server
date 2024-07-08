from django.urls import path
from . import views

urlpatterns = [
    path('job-detail/', views.job_detail_view, name='job_detail'),
]
