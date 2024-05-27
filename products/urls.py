from django.urls import path
from .products import AllProductsView, ProductDetailsView


app_name = "Products"

urlpatterns = [
    path("all", AllProductsView.as_view(), name="AllProductsUrl"),
    path("<slug:slug>", ProductDetailsView.as_view(), name="ProductDetailsUrl"),
]
