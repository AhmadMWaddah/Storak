from django.urls import path
from .products import AllProductsView, ProductDetailsView, CompareProductsView


app_name = "Products"

urlpatterns = [
    path("all", AllProductsView.as_view(), name="AllProductsUrl"),
    path("details", ProductDetailsView.as_view(), name="ProductDetailsUrl"),
    path("compare", CompareProductsView.as_view(), name="CompareProductsUrl"),
]
