from django.shortcuts import render, redirect, get_object_or_404
from students.models import StudentName
from .models import Schedule
from .forms import StudentScheduleForm
# Create your views here.
def schedule_list(request):
    schedule_list = Schedule.objects.all()
    context = {
        "title": "schedule list",
        "schedulelist": schedule_list,
    }
    return render(request, "schedules/schedule_list.html", context)
def schedule_student(request, pk):
    instance=get_object_or_404(StudentName, pk=pk)
    form = StudentScheduleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.user = request.user
        instance=form.save(commit=False)
        instance.save()
        return redirect('student:list')
    context = {
        "form": form,
        "title": "schedule student",
        "instance": instance,
    }
    return render(request, "students/student_schedule.html", context)