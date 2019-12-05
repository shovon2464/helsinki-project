from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from django.utils import timezone
from django.conf import settings


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
               email = self.normalize_email(email),
               username =username,
               password = password

            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
               email = self.normalize_email(email),
               username =username,

               password = password
           )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user










class Account(AbstractBaseUser):
    email                          = models.EmailField(verbose_name = "email", max_length=30, unique = True)
    username                       = models.CharField(max_length = 30, unique = True)
    date_joined                    = models.DateTimeField(verbose_name='date joined', auto_now_add = True)
    last_login                     = models.DateTimeField(verbose_name='last login', auto_now = True)
    is_admin                       = models.BooleanField(default = False)
    is_active                      = models.BooleanField(default = True)
    is_staff                       = models.BooleanField(default = False)
    is_superuser                   = models.BooleanField(default = False)


    full_name                      = models.CharField(max_length = 255)
    profile_picture                = models.ImageField(upload_to = 'profile_picture/', default='default.jpg')
    address                        = models.TextField()
    gender_choices                 = [('male', 'male'), ('female', 'female')]
    gender                         = models.CharField(max_length=10, choices=gender_choices)
    get_email_choices              = [('yes', 'yes'), ('no', 'no')]
    get_email                      = models.CharField(max_length=10, choices=get_email_choices)


    objects = MyAccountManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]




    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
