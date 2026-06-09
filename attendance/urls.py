from django.urls import path
from . import views

urlpatterns = [
    path('take/', 
        views.take_attendance, 
        name='take_attendance'),
    path('students/',
        views.get_students,
        name='attendance_students'),
    path('list/',
        views.attendance_list,
        name='attendance_list'),
    path('detail/<int:pk>',
        views.attendance_detail,
        name='attendance_detail'),
    path('delete/<int:pk>',
        views.delete_attendance,
        name='delete_attendance'),
]
