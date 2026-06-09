from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('add-subject', views.subject_create, name='subject_add'),
    path('update-subject/<int:pk>', views.subject_update, name='subject_update'),
    path('delete-subject/<int:pk>', views.subject_delete, name='subject_delete'),
]
