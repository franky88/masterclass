import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from sections.models import Section
from students.models import StudentName
from django.db.models import Count
# Create your models here.
class WeeklySchedule(models.Model):
    schedule = models.CharField(max_length=120, blank=True, null=True)
    def __str__(self):
        return self.schedule
class SubjectSchedule(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    subject_name = models.CharField(max_length=120, blank=True, null=True)
    schedule = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, blank=True, null=True)
    total_units = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    # def student_schedule_count(self):
    #     return self.student_schedule.count()
    # def student_cap(self):
    #     cap = self.max_number - int(self.student_schedule_count())
    #     return cap
    def total_time(self):
        # rendertime = self.end_time.second - self.start_time.second
        today = date.today()
        st = datetime.datetime.combine(today, self.start_time)
        et = datetime.datetime.combine(today, self.end_time)
        tt = et - st
        return tt
    def __str__(self):
        sched = "%s - %s"%(str(self.start_time),str(self.end_time))
        s = "%s - %s (%s)"%(self.section,self.subject_name, sched)
        return s.upper()
class StudentAdviceSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    student = models.ForeignKey(StudentName, on_delete=models.CASCADE, blank=True, null=True)
    schedule = models.ForeignKey(SubjectSchedule, on_delete=models.CASCADE, blank=True, null=True)
    advice = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s - %s"%(self.student, self.schedule)
