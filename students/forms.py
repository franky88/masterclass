from django import forms
from .models import StudentName
class StudentAddForm(forms.ModelForm):
    class Meta:
        model = StudentName
        fields = (
            "first_name",
            "middle_name",
            "last_name",
            "extension_name",
            "birth_date",
        )

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = StudentName
        fields = (
            "lrn",
            "first_name",
            "middle_name",
            "last_name",
            "extension_name",
            "birth_date",
            "schedule",
            "image",
            "school_status",
        )
# class StudentScheduleForm(forms.ModelForm):
#     class Meta:
#         model = StudentName
#         fields = (
#             "schedule",
#             "advice",
#             "remarks",
#         )