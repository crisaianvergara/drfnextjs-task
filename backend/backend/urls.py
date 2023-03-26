from django.contrib import admin
from django.urls import path, include
from scan_api import urls as scan_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scans/", include(scan_urls)),
]
