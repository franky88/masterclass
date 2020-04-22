from django import forms
from .models import SubjectSchedule
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = SubjectSchedule
        fields = [
            "section",
            "subject_name",
            "start_time",
            "end_time"
        ]
# class ScheduleAdviceForm(forms.ModelForm):
#     class Meta:
#         model = ScheduleAdvice
#         fields = [
#             "schedule",
#             "advice",
#             "remarks",
#         ]