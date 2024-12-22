from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('register/', views.RegisterUserView.as_view(), name='register-user'),
]
