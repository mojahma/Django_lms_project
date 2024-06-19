from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  
    external_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


# Added Models(NEW CODE)
 
class CourseSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    selected_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'


# Added Models(NEW CODE)
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
   
    
    
class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress_percentage = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.progress_percentage}%'
    
class CalendarEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.title
    

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.score}'
    
class Quiz(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'Quiz for {self.lesson.title}'


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.text  