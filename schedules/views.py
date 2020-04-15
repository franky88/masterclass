from django.shortcuts import render, redirect, get_object_or_404
from students.models import StudentName
from .models import Schedule
from .forms import ScheduleForm
# Create your views here.
def schedule_list(request):
    schedule_list = Schedule.objects.all()
    context = {
        "title": "schedule list",
        "schedulelist": schedule_list,
    }
    return render(request, "schedules/schedule_list.html", context)
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