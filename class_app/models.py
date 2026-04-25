from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="videos")
    file = models.FileField(upload_to='course_videos/',blank=False)

    def __str__(self):
        return f'{self.title} - {self.course}'

class Quiz(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="quizzes")
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.course} - {self.question}'
    
class Enrollment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'