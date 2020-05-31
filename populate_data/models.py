from django.db import models
import datetime
from django.utils import timezone
import tzlocal
import uuid


# Create your models here.

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=uuid.uuid4().hex[:8].upper(), editable=False)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200, default=tzlocal.get_localzone().zone)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    real_name = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject
