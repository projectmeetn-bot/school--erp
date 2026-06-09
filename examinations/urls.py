from django.urls import path
from . import views

urlpatterns = [

    # Examination CRUD
    path(
        '',
        views.examination_list,
        name='examination_list'
    ),

    path(
        'add/',
        views.examination_add,
        name='examination_add'
    ),

    path(
        'edit/<int:pk>/',
        views.examination_edit,
        name='examination_edit'
    ),

    path(
        'delete/<int:pk>/',
        views.examination_delete,
        name='examination_delete'
    ),

    # Student Examination
    path(
        'student/',
        views.student_examinations,
        name='student_examinations'
    ),

    path(
        'apply/<int:exam_id>/',
        views.apply_exam,
        name='apply_exam'
    ),

    path(
        'my-applications/',
        views.my_applications,
        name='my_applications'
    ),

    path(
        'my-halltickets/',
        views.my_halltickets,
        name='my_halltickets'
    ),

    # Exam Applications
    path(
        'applications/',
        views.application_list,
        name='application_list'
    ),

    path(
        'approve/<int:pk>/',
        views.approve_application,
        name='approve_application'
    ),

    path(
        'reject/<int:pk>/',
        views.reject_application,
        name='reject_application'
    ),

    # Hall Tickets
    path(
        'halltickets/',
        views.hallticket_list,
        name='hallticket_list'
    ),

    path(
        'hallticket/delete/<int:pk>/',
        views.hallticket_delete,
        name='hallticket_delete'
    ),

    path(
        'hallticket/pdf/<int:pk>/',
        views.hallticket_pdf,
        name='hallticket_pdf'
    ),
]