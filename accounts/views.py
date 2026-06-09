from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from classes.models import ClassRoom


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)

            if user.role == "admin":
                return redirect("admin_dashboard")

            elif user.role == "teacher":
                return redirect("teacher_dashboard")

            elif user.role == "student":
                return redirect("student_dashboard")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def admin_dashboard(request):

    if request.user.role != "admin":
        return redirect("login")

    context = {
        "student_count": Student.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "subject_count": Subject.objects.count(),
        "class_count": ClassRoom.objects.count(),
    }

    return render(
        request,
        "accounts/admin_dashboard.html",
        context
    )


@login_required(login_url='login')
def teacher_dashboard(request):

    if request.user.role != "teacher":
        return redirect("login")

    context = {
        "student_count": Student.objects.count(),
        "subject_count": Subject.objects.count(),
        "class_count": ClassRoom.objects.count(),
    }

    return render(
        request,
        "accounts/teacher_dashboard.html",
        context
    )


@login_required(login_url='login')
def student_dashboard(request):

    if request.user.role != "student":
        return redirect("login")

    return render(
        request,
        "accounts/student_dashboard.html"
    )


@login_required(login_url='login')
def home_redirect(request):

    if request.user.role == "admin":
        return redirect("admin_dashboard")

    elif request.user.role == "teacher":
        return redirect("teacher_dashboard")

    elif request.user.role == "student":
        return redirect("student_dashboard")

    return redirect("login")