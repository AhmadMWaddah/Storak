from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("humans/", include("humans.urls", namespace="Humans")),
    path("categories/", include("categories.urls", namespace="Categories")),
    path("products/", include("products.urls", namespace="Products")),
    path("bag/", include("bags.urls", namespace="Bags")),
    path("order/", include("orders.urls", namespace="Orders")),
    path("DashBoard/", admin.site.urls),
    path("", include("pages.urls", namespace="Pages")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
