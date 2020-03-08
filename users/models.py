from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    TEAMS = (
        ('none', _('NBA')),
        ('pelicans', _('New Orleans Pelicans')),
        ('lakers', _('Los Angeles Lakers')),
        ('celtics', _('Boston Celtics')),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    team = models.CharField(
        max_length=32,
        choices=TEAMS,
        default='none',
        )
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username