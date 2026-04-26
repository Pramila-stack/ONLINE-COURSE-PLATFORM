
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class QuizForm(forms.Form):
    def __init__(self,*args,**kwargs):
        quiz = kwargs.pop('quiz')
        super().__init__(*args,**kwargs)
        self.fields['answer'] = forms.ChoiceField(
            choices = [
                (1, quiz.option1),
                (2, quiz.option2),
                (3, quiz.option3),
                (4, quiz.option4),
            ],
            widget=forms.RadioSelect,
            label=quiz.question
        )
        