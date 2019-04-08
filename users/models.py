from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    TypeOfUserAccount = (
    ('ST', 'Student'), #student
    ('SA', 'Staff'), #staff
    ('PR', 'Professor'), # prof
    ('Fr', 'Externer Student'), #foreign
    )

    FK = (
    ('FK01', 'Fakultät 01'),  
    ('FK02', 'Fakultät 02'),  
    ('FK03', 'Fakultät 03'),  
    ('FK04', 'Fakultät 04'),  
    ('FK05', 'Fakultät 05'),  
    ('FK06', 'Fakultät 06'),  
    ('FK07', 'Fakultät 07'),  
    ('FK08', 'Fakultät 08'),  
    ('FK09', 'Fakultät 09'),  
    ('FK10', 'Fakultät 10'),  
    ('FK11', 'Fakultät 11'),  
    ('FK12', 'Fakultät 12'),  
    ('FK13', 'Fakultät 13'),  
    ('FK14', 'Fakultät 14'),  
    )

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    typOfAccount = models.CharField(
        max_length=2,
        choices=TypeOfUserAccount,
        default='ST',
    )
    Fakultaet = models.CharField(
        max_length=4,
        choices=FK,
        default='FK07',
    )
    verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def getUserName(self):
        return str(self.email)


