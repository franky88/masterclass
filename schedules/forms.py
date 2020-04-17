from django import forms
from .models import Schedule
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            "section",
            "schedule_name",
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