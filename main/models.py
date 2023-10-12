# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser


# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     role=models.CharField(max_length=100,default='student',unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] 

#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,username, email, password=None, role='student', **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password=None, role='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username,email, password, role, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, default='student')
    # Add other fields as needed

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
