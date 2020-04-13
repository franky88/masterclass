from django.shortcuts import render
from .models import Section
# Create your views here.
def section_list(request):
    section_list=Section.objects.all().order_by('section_name')
    context = {
        "title": "section list",
        "sectionlist": section_list,
    }
    return render(request, "sections/section_list.html", context)