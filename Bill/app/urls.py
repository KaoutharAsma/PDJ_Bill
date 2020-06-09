from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path

urlpatterns = [
    path('bill/', include('bill.urls')),
    path('admin/', admin.site.urls),
]
