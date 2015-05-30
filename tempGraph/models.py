from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Readings(models.Model):
	temp = models.DecimalField(decimal_places=2,max_digits=5, default=0)
	time = models.DateTimeField(default=timezone.now)

	class Meta:
		get_latest_by = 'time'