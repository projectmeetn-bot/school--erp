from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add-student/', views.student_create, name='student_add'),
    path('edit-student/<int:pk>', views.student_update, name='student_update'),
    path('delete-student/<int:pk>', views.student_delete, name='student_delete'),
]
