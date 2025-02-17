"""
Custom User model for Django

This module defines a custom user model NewUser that extends Django's 
AbstractBaseUser and PermissionsMixin.

The CustomAccountManager class is for user creation, functionality to
create both regular users and superusers.

"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class CustomAccountManager(BaseUserManager):
    """
    Since Djangos default user manager (UserManager) doesnt work with a 
    custom user model, this custom manager is used instead.
    """

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Custom function to create a regular user. 

        :param self: 
        :param email: 
        :param user_name:
        :param first_name:
        :param password:
        :param other_fields:
        """

        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """
        Custom function to create a new superuser. 

        :param self: 
        :param email: 
        :param user_name:
        :param first_name:
        :param password:
        :param other_fields:
        """

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(
                "SuperUser must be assigned to is_staff = True"
            )
        if other_fields.get("is_superuser") is not True:
            raise ValueError (
                "Superuser must be assigned to is_superuser = True"
            )
        return self.create_user(email, user_name, first_name, password, **other_fields)



class NewUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom Django user model class for a new user. 

    :param AbstractBaseUser: Django class for creating custom user model
    :param PermissionsMixin: Django mixin for user auth and permissions.
    """

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    about = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    phone_number = PhoneNumberField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return str(self.email)
