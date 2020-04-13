from django.contrib import admin
from .models import Section
# Register your models here.
@admin.register(Section)
class SectionAdminList(admin.ModelAdmin):
    list_display = ['__str__']