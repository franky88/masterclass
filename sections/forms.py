from django import forms
from .models import Section
class SectionAddForms(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            "adviser",
            "section_name",
            "grade_level",
            "max_number",
            "student_counter",
        ]