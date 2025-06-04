from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    full_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    next_of_kin_name = models.CharField(max_length=255)
    next_of_kin_address = models.TextField()
    next_of_kin_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username
