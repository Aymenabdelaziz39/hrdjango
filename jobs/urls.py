from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.JobPostView.as_view(), name='job-list'),
    path('create/', views.JobPostView.as_view(), name='job-create'),
    path('applications/<int:job_post_id>/', views.ApplicationView.as_view(), name='job-applications'),
]
