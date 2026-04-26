from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,View

from .models import Course, Enrollment, Quiz

from .forms import QuizForm, SignupForm
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
    
class NotEnrollView(LoginRequiredMixin,View):
    def post(self,request,pk):
        course = get_object_or_404(Course,pk=pk)
        Enrollment.objects.filter(user=self.request.user,course=course).delete()
        return redirect("course-list")

class DashBoardView(LoginRequiredMixin,ListView):
    model = Enrollment
    template_name = "dashboard.html"
    context_object_name = "enrollments"

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)
    

class QuizView(LoginRequiredMixin,View):
    template_name = "quiz.html"

    def get(self,request,course_pk,quiz_pk):
        quiz = get_object_or_404(Quiz,pk=quiz_pk,course_id=course_pk)
        form = QuizForm(quiz=quiz)


        #For next quiz navigation.
        quizzes = list(quiz.course.quizzes.all().order_by("-id"))
        current_index = quizzes.index(quiz)
        next_quiz = (
            quizzes[current_index + 1] if current_index + 1 < len(quizzes) else None
        )

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'quiz':quiz,
                'correct':None,
                'next_quiz':next_quiz,
                'course_pk':course_pk,
            },
        )
    
    def post(self,request,course_pk,quiz_pk):
        quiz = get_object_or_404(Quiz,pk=quiz_pk,course_id=course_pk)
        form = QuizForm(request.POST,quiz=quiz)
        correct = None
        if form.is_valid():
            answer = int(form.cleaned_data['answer'])
            correct = answer == quiz.correct_option

            #For next quiz navigation.
            quizzes = list(quiz.course.quizzes.all().order_by("-id"))
            current_index = quizzes.index(quiz)
            next_quiz = (
                quizzes[current_index + 1] if current_index + 1 < len(quizzes) else None
            )

            return render(
                request,
                self.template_name,
                {
                    'form' : form,
                    "quiz" : quiz,
                    "correct":correct,
                    "next_quiz":next_quiz,
                    "course_pk":course_pk
                },
            )



    



    