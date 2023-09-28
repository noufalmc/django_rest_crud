
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/crud/', include("api.v1.crud.urls", namespace="api_v1_crud")),

]
