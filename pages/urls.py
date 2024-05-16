from django.urls import path
from .pages import HomeView, NotFoundView

app_name = "Pages"

urlpatterns = [
    path("", HomeView.as_view(), name="HomeUrl"),
    path("404", NotFoundView.as_view(), name="NotFoundUrl"),
]
