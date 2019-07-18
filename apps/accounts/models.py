from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import pre_save


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email cannot be blank.')
        
        if not password:
            raise ValueError('Password cannot be blank.')
        
        user = self.model(
            email= self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user  = self.create_user(email, password=password)
        user.staff = True
        user = user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.staff = True
        user.admin = True
        user = user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    admin = models.BooleanField(default=False)
    student = models.BooleanField(verbose_name='As a Student', default=False)
    instructor = models.BooleanField(verbose_name='As an Instructor', default=False)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def get_fullname(self):
        return self.email

    def get_shortname(self):
        return self.email.split('@')[0]

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

def pre_save_listener(sender, instance, *args, **kwargs):
    if instance.student:
        instance.instructor = False
    if instance.instructor:
        instance.student = False

pre_save.connect(receiver=pre_save_listener, sender=User)

