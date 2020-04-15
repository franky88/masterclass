import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
GRADE_LEVEL = [
    ("NGSP", "Non-graded SPED"),
    ("SP", "SPED"),
    ("ALS", "ALT LEARNING SYSTEM"),
    ("NU", "NURSERY"),
    ("K", "Kindergarten"),
    ("G1", "Grade 1"),
    ("G2", "Grade 2"),
    ("G3", "Grade 3"),
    ("G4", "Grade 4"),
    ("G5", "Grade 5"),
    ("G6", "Grade 6"),
]
class Section(models.Model):
    adviser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    section_name = models.CharField(max_length=120, unique=True)
    grade_level = models.CharField(max_length=60, choices=GRADE_LEVEL, blank=True,null=True)
    max_number = models.IntegerField(verbose_name="maximum number of students", default=0)
    student_counter = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.section_name
