from django.urls import path
from .views import validate_user_email

app_name = 'account'
urlpatterns = [
    path("otp-validation/<str:email>/", validate_user_email, name='validate'),
]