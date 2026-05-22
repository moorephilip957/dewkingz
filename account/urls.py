from django.urls import path
from .views import validate_user_email

app_name = 'account'
urlpatterns = [
    path("validate-user-otp/<str:email>/", validate_user_email, name='validate'),
]