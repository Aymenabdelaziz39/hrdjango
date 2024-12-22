from django.urls import path
from .views import ResumeMatcherView

urlpatterns = [
    path('match-resume/', ResumeMatcherView.as_view(), name='match-resume'),
]


