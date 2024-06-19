from django.urls import path
from . import views
from .views import custom_login_view, dashboard_view

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('courses/', views.courses_selected_view, name='courses_selected'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('progress/', views.progress_view, name='progress'),
    path('login/', custom_login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
