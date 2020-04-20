from django.shortcuts import render, redirect, get_object_or_404
from .models import Section
from .forms import SectionAddForms
# Create your views here.
def section_list(request):
    section_list=Section.objects.all().order_by('section_name')
    context = {
        "title": "section list",
        "sectionlist": section_list,
    }
    return render(request, "sections/section_list.html", context)

def add_section(request):
    form = SectionAddForms(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
        return redirect("section:list")
    context = {
        "title": "add schedule",
        "form": form,
        # "count": student_count,
    }
    return render(request, "sections/add_section.html", context)
def section_details(request, pk):
    instance = get_object_or_404(Section, pk=pk)
    context = {
        "title": "section details",
        "instance": instance,
    }
    return render(request, "sections/section_detail.html", context)