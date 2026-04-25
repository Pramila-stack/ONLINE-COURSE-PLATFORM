from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,View

from .models import Course, Enrollment

from .forms import SignupForm
from django.contrib.auth import login
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)

class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.all().order_by("-created_at")
    
class CourseDetailView(LoginRequiredMixin,DetailView):
    model = Course
    template_name = "course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrolled'] = Enrollment.objects.filter(user=self.request.user,course=self.object).exists()
        return context

class EnrollView(LoginRequiredMixin,View):
    def post(self,request,pk):
        course = get_object_or_404(Course,pk=pk)
        Enrollment.objects.get_or_create(user=self.request.user,course=course)
        return redirect("course-detail",pk=pk)
    
class DashBoardView(LoginRequiredMixin,ListView):
    model = Enrollment
    template_name = "dashboard.html"
    context_object_name = "enrollment"

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)


    



    