import os
import sys
from django.db import models
from django.utils import timezone

def file_path(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000

    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class File(models.Model):
    name = models.CharField(max_length=200)
    metadata_uuid = models.CharField(max_length=200)
    file = models.FileField(upload_to=file_path)

    def __str__(self):
        return self.name