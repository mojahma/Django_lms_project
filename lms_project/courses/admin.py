from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Course, Lesson, Notification, CourseSelection, UserProgress, CalendarEvent, LeaderboardEntry

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="50px">')
        else:
            return 'No Image'

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'content')
    list_filter = ('course',)
    search_fields = ('title', 'content')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')

@admin.register(CourseSelection)
class CourseSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'selected_date')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'progress_percentage')

@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_datetime', 'end_datetime')

@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
