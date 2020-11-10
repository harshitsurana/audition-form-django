from django import forms
from .models import Profile, State
from django.contrib.auth.models import User
from myauth.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from forms.choice import GENDER_CHOICES

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,label_suffix=" / Email Id")
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[EmailValidator(message="Enter a valid Email address",code=None,whitelist=None)])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already registered")
        return email

class ProfileRegisterForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Profile
        fields = ['name','gender','mobile','college','country','state','city','github','codechef', 'bio','image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')