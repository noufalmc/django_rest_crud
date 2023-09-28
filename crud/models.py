from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel


# Create your models here.
class BloodGroup(BaseModel):
    blood_group = models.CharField(max_length=128)

    class Meta:
        db_table = 'crud_blood_group'
        verbose_name = _('blood_group')
        verbose_name_plural = _('blood_groups')
        ordering = ('-created_at',)

    def __str__(self):
        return self.blood_group


class BloodData(BaseModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField()
    willing_to_donate = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to="profile")

    class Meta:
        db_table = 'crud_blood_data'
        verbose_name = _('blood_data')
        verbose_name_plural = _('blood_datas')
        ordering = ('-created_at',)
