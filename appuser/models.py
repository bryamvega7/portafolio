from django.db import models

# Create your models here.
class IpData(models.Model):
    ip = models.CharField(max_length=100)