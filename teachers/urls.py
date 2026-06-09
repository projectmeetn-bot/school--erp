from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('add-teacher/', views.teacher_create, name='teacher_add'),
    path('edit-teacher/<int:pk>', views.teacher_update, name='teacher_update'),
    path('delete-teacher/<int:pk>', views.teacher_delete, name='teacher_delete'),
]
