from django.contrib import admin
from django.urls import path


from class_app import views 

urlpatterns = [
    path("",views.CourseListView.as_view(),name="course-list"),
    path("signup/",views.SignupView.as_view(),name="signup"),
    path("course-detail/<int:pk>/",views.CourseDetailView.as_view(),name='course-detail'),
    path("enroll/<int:pk>/",views.EnrollView.as_view(),name="enroll"),
    path("noenroll/<int:pk>/",views.NotEnrollView.as_view(),name="noenroll"),
    path("dashboard/",views.DashBoardView.as_view(),name="dashboard"),
    path("course/<int:course_pk>/quiz/<int:quiz_pk>/",views.QuizView.as_view(),name="quiz")
]
