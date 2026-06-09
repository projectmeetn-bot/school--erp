from django.urls import path
from . import views

urlpatterns = [
    path('',
        views.timetable_list,
        name='timetable_list'),
    
    path('generate/<int:classroom_id>/',
        views.generate_timetable,
        name='generate_timetable'),
    
    path('class/<int:classroom_id>/',
        views.class_timetable,
        name='class_timetable'),
    
    path('edit/<int:pk>/',
        views.timetable_edit,
        name='timetable_edit'),
    
    path('delete/<int:pk>/',
        views.timetable_delete,
        name='timetable_delete'),
]
