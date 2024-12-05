from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_super_admin():
                return redirect('super_admin_dashboard')
            elif user.is_admin():
                return redirect('admin_dashboard')
            elif user.is_viewer():
                return redirect('viewer_dashboard')
            else:
                return HttpResponseForbidden("You don't have permission to view this page.")
        else:
            return render(request, 'app_base/login.html', {'error': 'Invalid credentials'})
    return render(request, 'app_base/login.html')


def super_admin_required(user):
    return user.is_authenticated and getattr(user, 'is_super_admin', False)


def admin_required(user):
    return user.is_authenticated and (
            getattr(user, 'is_super_admin', False) or getattr(user, 'is_admin', False)
    )


@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    viewers = CustomUser.objects.filter(role='viewer')
    error = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = CustomUser.objects.create(
                username=username,
                password=make_password(password),
                email=email,
                role='viewer'
            )
            user.save()
        except Exception as e:
            error = str(e)

    return render(request, 'app_base/dashboard_admin.html', {'viewers': viewers, 'error': error})


@login_required
@user_passes_test(super_admin_required)
def super_admin_dashboard(request):
    admin_users = CustomUser.objects.filter(role__in=['admin', 'super_admin'])
    error = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST['role']
        if role not in ['admin', 'super_admin']:
            error = 'Invalid role'
        else:
            try:
                user = CustomUser.objects.create(
                    username=username,
                    password=make_password(password),
                    email=email,
                    role=role
                )
                user.save()
            except Exception as e:
                error = str(e)

    return render(request, 'app_base/dashboard_super_admin.html', {'admin_users': admin_users, 'error': error})


@login_required
def dashboard_view(request):
    if request.user.is_super_admin():
        return render(request, 'app_base/dashboard_super_admin.html')
    elif request.user.is_admin():
        return render(request, 'app_base/dashboard_admin.html')
    elif request.user.is_viewer():
        return render(request, 'app_base/dashboard_viewer.html')
    else:
        return HttpResponseForbidden("You don't have permission to view this page")


@login_required
def viewer_dashboard(request):
    return render(request, 'app_base/dashboard_viewer.html')
