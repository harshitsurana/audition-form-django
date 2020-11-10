from django.db import models
from django.contrib.auth.models import User
from forms.choice import GENDER_CHOICES
from django.core.validators import MinLengthValidator, URLValidator, MinLengthValidator, MaxLengthValidator

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=50, null=True, validators=[MinLengthValidator(2,"Enter Full Name")])
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6,null=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    mobile = models.CharField(null=True,max_length=10,validators=[MinLengthValidator(10, "Enter a valid 10 digit mobile number"),MaxLengthValidator(10,"Enter a valid 10 digit mobile number")])
    college = models.CharField("College", max_length=50, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True,blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    codechef = models.URLField(validators=[URLValidator(schemes=None)],null=True,blank=True)
    github = models.URLField(validators=[URLValidator(schemes=None)],null=True,blank=True)
    bio = models.CharField("Bio", max_length=100, blank=True)

    def __str__(self):
        return self.user.username