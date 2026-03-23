
# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Student, Attendance
from .forms import StudentForm, AttendanceForm

# ---- Student CRUD ----
def student_list(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return JsonResponse({
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "student_id": student.student_id
    })

def student_create(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        student = form.save()
        return JsonResponse({"id": student.id})
    return JsonResponse({"errors": form.errors})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        student = form.save()
        return JsonResponse({"id": student.id})
    return JsonResponse({"errors": form.errors})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return JsonResponse({"deleted": True})

# ---- Attendance CRUD ----
def attendance_list(request):
    attendance = list(Attendance.objects.values())
    return JsonResponse(attendance, safe=False)

def attendance_detail(request, pk):
    att = get_object_or_404(Attendance, pk=pk)
    return JsonResponse({
        "id": att.id,
        "student": str(att.student),
        "date": att.date,
        "status": att.status
    })

def attendance_create(request):
    form = AttendanceForm(request.POST)
    if form.is_valid():
        att = form.save()
        return JsonResponse({"id": att.id})
    return JsonResponse({"errors": form.errors})

def attendance_update(request, pk):
    att = get_object_or_404(Attendance, pk=pk)
    form = AttendanceForm(request.POST, instance=att)
    if form.is_valid():
        att = form.save()
        return JsonResponse({"id": att.id})
    return JsonResponse({"errors": form.errors})

def attendance_delete(request, pk):
    att = get_object_or_404(Attendance, pk=pk)
    att.delete()
    return JsonResponse({"deleted": True})
