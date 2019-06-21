from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Schedule

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ['posted_time', 'pub_date']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
    }
class ProfileForm(forms.ModelForm):

    class Meta:
        model =Profile
        exclude=['user']

 
