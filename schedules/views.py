from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from students.models import StudentName
from .models import SubjectSchedule, StudentAdviceSchedule
from .forms import ScheduleForm
# Create your views here.
def schedule_list(request):
    schedule_list = SubjectSchedule.objects.all()
    context = {
        "title": "schedule list",
        "schedulelist": schedule_list,
    }
    return render(request, "schedules/schedule_list.html", context)
def schedule_detail(request, pk):
    instance = get_object_or_404(SubjectSchedule, pk=pk)
    context = {
        "title": "schedule detail",
        "instance": instance,
    }
    return render(request, "schedules/schedule_detail.html", context)
def add_schedule(request):
    form = ScheduleForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('schedule:list')
    context = {
        "title": "add schedule",
        "form": form,
    }
    return render(request, "schedules/add_schedule.html", context)
def advice_student(request, pk):
    student = get_object_or_404(StudentName, pk=pk)
    studentScheduleFormset = inlineformset_factory(StudentName, StudentAdviceSchedule, fields=('schedule', 'advice', 'remarks'), max_num=1, can_delete=False)
    if request.method == "POST":
        formset = studentScheduleFormset(request.POST or None, request.FILES or None, instance=student)
        if formset.is_valid():
            formset.user = request.user
            formset.save()
            return redirect("student:list")
    formset = studentScheduleFormset(instance=student)
    context = {
        "formset": formset,
        "title": "advice student",
        "instance": student,
    }
    return render(request, "schedules/advice_student.html", context)