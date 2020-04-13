import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Section(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    section_name = models.CharField(max_length=120, unique=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.section_name
