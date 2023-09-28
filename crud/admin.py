from django.contrib import admin
from .models import BloodGroup, BloodData


# Register your models here.
class BloodGroupView(admin.ModelAdmin):
    list_display = ('id', 'blood_group', 'created_at', 'updated_at', 'is_deleted')
    list_display_links = ('blood_group',)


admin.site.register(BloodGroup, BloodGroupView)


class BloodDataView(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'mobile_number', 'willing_to_donate',
                    'blood_group', 'created_at', 'updated_at', 'is_deleted')
    list_display_links = ('blood_group',)


admin.site.register(BloodData, BloodDataView)
