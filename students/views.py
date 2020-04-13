from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import StudentName
from .forms import StudentAddForm, StudentEditForm, StudentScheduleForm
# Create your views here.
def my_list(request):
    student_list = StudentName.objects.all()
    student_adviced = StudentName.objects.filter(advice=True)
    student_toadviced = StudentName.objects.filter(advice=False)
    context = {
        "title": "my students",
        "studentlist": student_list,
		"studentadviced": student_adviced,
		"studenttoadviced": student_toadviced,
    }
    return render(request, "students/student_list.html", context)
def student_detail(request, pk):
	student_instance = get_object_or_404(StudentName, pk=pk)
	context = {
		"title": "student details",
		"instance": student_instance,
	}
	return render(request, "students/student_detail.html", context)
def student_add(request):
    form = StudentAddForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect("student:list")
    context = {
        "title": "register student",
        "form": form,
    }
    return render(request, "students/student_add.html", context)
def student_edit(request, pk):
	instance=get_object_or_404(StudentName, pk=pk)
	form = StudentEditForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('student:detail', pk=instance.pk)
	context = {
		"form": form,
		"title": "edit student",
		"instance": instance,
	}
	return render(request, "students/student_edit.html", context)
def student_update(request, pk):
	instance=get_object_or_404(StudentName, pk=pk)
	form = StudentEditForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('student:list')
	context = {
		"form": form,
		"title": "edit student",
		"instance": instance,
	}
	return render(request, "students/student_edit.html", context)
def delete_student(request, pk):
    instance = get_object_or_404(StudentName, pk=pk)
    instance.delete()
    return redirect("student:list")
def schedule_student(request, pk):
	instance=get_object_or_404(StudentName, pk=pk)
	form = StudentScheduleForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('student:list')
	context = {
		"form": form,
		"title": "schedule student",
		"instance": instance,
	}
	return render(request, "students/student_schedule.html", context)