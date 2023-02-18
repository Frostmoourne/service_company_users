import uuid

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy


class CustomUserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(gettext_lazy('username'), db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(gettext_lazy('active'), default=True)
    is_staff = models.BooleanField(gettext_lazy('staff status'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name=gettext_lazy('last login'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = CustomUserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """

        return str(self.userprofile) if hasattr(self, 'userprofile') else self.username

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'user\".\"users'
        verbose_name = gettext_lazy('user')
        verbose_name_plural = gettext_lazy('users')


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title


class PersonalAccount(models.Model):
    number = models.CharField(max_length=50)
    owners = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )
    allowed_persons = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )
    is_active = models.BooleanField(default=True)
    balance = models.FloatField()

    def __str__(self):
        return self.number
