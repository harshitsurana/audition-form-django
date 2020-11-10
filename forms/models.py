from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator, MaxLengthValidator, URLValidator
from django.contrib.auth.models import User
from django.conf import settings
from .choice import GENDER_CHOICES, BRANCH_CHOICES

class Form(models.Model) :
    name = models.CharField(max_length=50,validators=[MinLengthValidator(2, "Name must be greater than 2 characters")])
    email = models.EmailField(null=True,validators=[EmailValidator(message="Enter a valid Email address",code=None,whitelist=None)])
    mobile = models.CharField(null=True,max_length=10,validators=[MinLengthValidator(10, "Enter a valid 10 digit mobile number"),MaxLengthValidator(10,"Enter a valid 10 digit mobile number")])
    rollno = models.CharField(max_length=10,null=True)
    website = models.URLField(validators=[URLValidator(schemes=None)],null=True,blank=True)
    branch = models.CharField(choices=BRANCH_CHOICES,max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='images/',null=True)
    
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.name