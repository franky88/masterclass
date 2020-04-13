from django.contrib import admin
from .models import Schedule
# Register your models here.
@admin.register(Schedule)
class ScheduleAdminList(admin.ModelAdmin):
    list_display = ['__str__']