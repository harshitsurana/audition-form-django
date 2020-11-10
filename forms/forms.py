from django import forms
from .models import Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .choice import GENDER_CHOICES

class CreateForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Form
        fields = ['name', 'email','rollno', 'mobile', 'branch', 'gender', 'website','profile_img']

class UserRegisterForm(UserCreationForm):

  class Meta:
      model = User
      fields = ['username']