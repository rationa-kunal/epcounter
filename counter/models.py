from django.db import models
from django.contrib.auth.models import User


class Serial(models.Model):
    
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    season = models.IntegerField(default=0)
    counter = models.IntegerField(default=0)
    is_complete = models.BooleanField(default=False)