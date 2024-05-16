from django.urls import path
from .humans import SignUpView, SignInView, AccountView


app_name = "Humans"


urlpatterns = [
    path("sign-up", SignUpView.as_view(), name="SignUpUrl"),
    path("sign-in", SignInView.as_view(), name="SignInUrl"),
    path("my-account", AccountView.as_view(), name="AccountUrl"),
]
