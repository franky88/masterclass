from django.contrib import admin
from .models import SubjectSchedule, WeeklySchedule
# Register your models here.
@admin.register(SubjectSchedule)
class ScheduleAdminList(admin.ModelAdmin):
    list_display = ['__str__']
@admin.register(WeeklySchedule)
class WeeklyScheduleAdminList(admin.ModelAdmin):
    list_display = ['__str__']