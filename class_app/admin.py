from django.contrib import admin

from class_app.models import Course, Enrollment, Quiz, Video

# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Quiz)
admin.site.register(Enrollment)

