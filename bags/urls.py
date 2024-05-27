from django.urls import path
from .bags import BagView


app_name = "Bags"

urlpatterns = [
    path("bag", BagView.as_view(), name="BagUrl"),
]
