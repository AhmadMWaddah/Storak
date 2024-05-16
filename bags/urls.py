from django.urls import path
from .bags import BagView, WishListView, CheckOutView


app_name = "Bags"

urlpatterns = [
    path("wishlist", WishListView.as_view(), name="WishListUrl"),
    path("bag", BagView.as_view(), name="BagUrl"),
    path("checkout", CheckOutView.as_view(), name="CheckOutUrl"),
]
