from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SchoolName(models.Model):
    school_name = models.CharField(max_length=255)
    school_head = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
class SchoolYear(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_start = models.DateField()
    date_end = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s - %s"%(str(self.date_start.year), str(self.date_end.year))