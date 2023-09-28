from django.urls import path, include, re_path
from .views import BloodDataView, BloodDataDetailView

app_name = "crud"

urlpatterns = [
    path('', BloodDataView.as_view(), name="blood_data"),
    path('details/<uuid:pk>/', BloodDataDetailView.as_view(), name="blood_data")

]
