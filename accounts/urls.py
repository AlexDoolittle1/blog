from django.urls import path
from .views import SignUpView

urlpattens = [
    path("signup/", SignUpView.as_view(), name="signup")
]