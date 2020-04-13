from django import forms
from .models import StudentSchedule

class StudentScheduleForm(forms.ModelForm):
    class Meta:
        model = StudentSchedule
        fields = (
            "schedule",
            "advice",
            "remarks",
        )