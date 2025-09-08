from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import date

# Create your models here.

class UserManager(BaseException):
    def create_user(self, first_name, last_name, email, password, birthday=None):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, birthday=birthday)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]+$', 'Letters only')])
    last_name = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]+$', 'Letters only')])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    # Ninja/Sensei bonus: Check age
    def is_at_least_13(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            return age >= 13
        return True