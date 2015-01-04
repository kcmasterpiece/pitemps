from django.db import models

# Create your models here.
class Readings(models.Model):
	temp = models.DecimalField(decimal_places=2,max_digits=5, default=0)
