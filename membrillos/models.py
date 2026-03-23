
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"