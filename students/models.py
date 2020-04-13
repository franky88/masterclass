import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from schedules.models import Schedule
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.schedule.section.user.id, filename)
class StudentName(models.Model):
    lrn = models.CharField(max_length=12, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120, blank=True)
    extension_name = models.CharField(max_length=10, blank=True)
    GENDER = [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    birth_date = models.DateField()
    school_status = models.BooleanField(default=True, verbose_name='schooling status')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    advice = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-timestamp']
    def calculate_age(self):
        today = date.today()
        born = self.birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age
    def full_name(self):
        if self.middle_name == False:
            fullname = "%s, %s %s"%(self.last_name, self.first_name, self.extension_name)
        elif self.extension_name == False:
            fullname = "%s, %s %s"%(self.last_name, self.first_name, self.middle_name)
        elif self.middle_name == False and self.extension_name == False:
            fullname = "%s, %s"%(self.last_name, self.first_name)
        else:
            fullname = "%s, %s %s %s"%(self.last_name, self.first_name, self.middle_name, self.extension_name)
        return fullname
    def __str__(self):
        return self.full_name().title()