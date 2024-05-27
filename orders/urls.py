from django.urls import path
from .orders import CheckOutView


app_name = "Orders"

urlpatterns = [
    path("checkout", CheckOutView.as_view(), name="CheckOutUrl"),
]
