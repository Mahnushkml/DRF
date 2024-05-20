from django.db import models

# Create your models here.

class Assets(models.Model):
    ip = models.CharField(max_length=100)
    management_category = models.CharField(max_length=100)
    network_category = models.CharField(max_length=100)
    group_user = models.CharField(max_length=100)
    group_owner = models.CharField(max_length=100)
    responsible_employee = models.CharField(max_length=100)
    physical_location = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    sub_service = models.CharField(max_length=100)
    access_type = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    os = models.CharField(max_length=100)

    unpatchable = models.CharField(max_length=100)
    ref_num = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    siem_log = models.CharField(max_length=300)

    def __str__(self):
        return self.ip