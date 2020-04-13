from django.shortcuts import render, redirect, get_object_or_404
from students.models import StudentName
from .models import Schedule
# Create your views here.
def schedule_list(request):
    schedule_list = Schedule.objects.all()
    context = {
        "title": "schedule list",
        "schedulelist": schedule_list,
    }
    return render(request, "schedules/schedule_list.html", context)