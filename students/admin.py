from django.contrib import admin
from .models import StudentName
# Register your models here.
admin.site.site_header = "Masterclass"
@admin.register(StudentName)
class StudentAdminList(admin.ModelAdmin):
    list_display = ['full_name']
    list_filter = ['timestamp']