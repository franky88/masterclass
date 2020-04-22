from django.contrib import admin
from .models import SchoolYear
# Register your models here.
@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ["__str__"]