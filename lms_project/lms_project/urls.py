from django.contrib import admin
from django.urls import path, include
from courses import views as course_views
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('register/', course_views.register, name='register'),
    path('contact/', course_views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', course_views.login_view, name='login'),
    path('', course_views.home, name='home'),
    # Added After
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('selected-courses/', views.courses_selected_view, name='courses_selected'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('progress/', views.progress_view, name='progress'),
]
