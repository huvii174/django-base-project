from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('viewer_dashboard/', views.viewer_dashboard, name='viewer_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('super-admin-dashboard/', views.super_admin_dashboard, name='super_admin_dashboard'),
]
