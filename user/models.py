from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from user.choices import *


class Profile(AbstractUser):
    slug = models.SlugField(null=False, unique=True)
    photo = models.ImageField(blank=True, null=True, upload_to='profile_photos')
    account_type = models.IntegerField(choices=ACCOUNT_TYPE, default=1)
    about = models.TextField(blank=True, null=True, default='No info')
    website_url = models.URLField(max_length=250, blank=True, null=True)
    facebook_url = models.URLField(max_length=250, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Profiles'
