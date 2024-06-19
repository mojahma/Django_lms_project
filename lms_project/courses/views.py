from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ContactForm
from .models import Course
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Course, Notification, LeaderboardEntry

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle contact form submission (e.g., send email)
            messages.success(request, 'Thank you for your message. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))



# Added views(testing)
@login_required
def dashboard_view(request):
    courses_selected = Course.objects.filter(selected_by=request.user)
    notifications = Notification.objects.filter(user=request.user)
    leaderboard = LeaderboardEntry.objects.all().order_by('-score')[:10]
    context = {
        'courses_selected': courses_selected,
        'notifications': notifications,
        'leaderboard': leaderboard,
    }
    return render(request, 'dashboard.html', context)

@login_required
def courses_selected_view(request):
    courses_selected = Course.objects.filter(selected_by=request.user)
    context = {
        'courses_selected': courses_selected,
    }
    return render(request, 'courses_selected.html', context)

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user)
    context = {
        'notifications': notifications,
    }
    return render(request, 'notifications.html', context)

@login_required
def leaderboard_view(request):
    leaderboard = LeaderboardEntry.objects.all().order_by('-score')[:10]
    context = {
        'leaderboard': leaderboard,
    }
    return render(request, 'leaderboard.html', context)

@login_required
def calendar_view(request):
    # Logic to fetch calendar events
    context = {
        # Add context variables as needed
    }
    return render(request, 'calendar.html', context)

@login_required
def progress_view(request):
    # Example progress calculation
    user_progress = 60  # Example: User progress percentage
    context = {
        'user_progress': user_progress,
    }
    return render(request, 'progress.html', context)

# additional when working
def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard upon successful login
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})