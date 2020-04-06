from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db.models.signals import pre_save
from django.utils.text import slugify

class CustomUser(AbstractUser):
    # TEAMS = (
    #     ('none', _('NBA')),
    #     ('hawks', _('Atlanta Hawks')),
    #     ('celtics', _('Boston Celtics')),
    #     ('nets', _('Brooklyn Nets')),
    #     ('hornets', _('Charlotte Hornets')),
    #     ('bulls', _('Chicago Bulls')),
    #     ('cavaliers', _('Cleveland Cavaliers')),
    #     ('mavericks', _('Dallas Mavericks')),
    #     ('nuggets', _('Denver Nuggets')),
    #     ('pistons', _('Denver Pistons')),
    #     ('warriors', _('Golden State Warriors')),
    #     ('rockets', _('Houston Rockets')),
    #     ('pacers', _('Indiana Pacers')),
    #     ('clippers', _('Los Angeles Clippers')),
    #     ('lakers', _('Los Angeles Lakers')),
    #     ('pelicans', _('New Orleans Pelicans')),
        
    # )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True)
    # team = models.CharField(
    #     max_length=32,
    #     choices=TEAMS,
    #     default='none',
    #     )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

def create_slug(instance, new_slug=None):
    slug = slugify(instance.username)
    if new_slug is not None:
        slug = new_slug
    qs = CustomUser.objects.filter(slug=slug).order_by("-pk")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_user_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_user_receiver, sender=CustomUser)