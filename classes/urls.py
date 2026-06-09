from django.urls import path
from . import views

urlpatterns = [
    path('', 
         views.classroom_list,
         name='classroom_list'
         ),
    path('add-classroom', 
         views.classroom_create,
         name='classroom_add'
         ),
    path('update-classroom/<int:pk>', 
         views.classroom_update,
         name='classroom_update'
         ),
    path('delete-classroom/<int:pk>', 
         views.classroom_delete,
         name='classroom_delete'
         ),
]
