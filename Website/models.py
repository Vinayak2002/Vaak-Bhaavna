from django.db import models
import uuid
from django.urls.base import reverse
# Create your models here.
class Audio_store(models.Model):
    record=models.FileField(upload_to='documents/')
    class Meta:
        db_table='Audio_store'