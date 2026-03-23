
from django.urls import path
from . import views

urlpatterns = [
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # Attendance URLs
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/<int:pk>/', views.attendance_detail, name='attendance_detail'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/update/<int:pk>/', views.attendance_update, name='attendance_update'),
    path('attendance/delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
]