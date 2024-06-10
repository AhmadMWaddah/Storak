from django.urls import path
from .bags import BagDetailsView, AddToBagView, UpdateBagItemView, remove_from_bag_view

app_name = "Bags"


urlpatterns = [
    path("details", BagDetailsView.as_view(), name="BagDetailsUrl"),
    path("add-to-bag/<slug:slug>", AddToBagView.as_view(), name="AddToBagUrl"),
    path(
        "update-in-bag/<slug:slug>",
        UpdateBagItemView.as_view(),
        name="UpdateBagItemUrl",
    ),
    path(
        "remove-from-bag/<slug:slug>",
        remove_from_bag_view,
        name="RemoveFromBagUrl",
    ),
]
