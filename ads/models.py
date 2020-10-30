from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from tinymce.models import HTMLField


class Created(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Ad(Created):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='ad_images/')
    short_description = models.TextField(null=False, blank=False, max_length=300)
    long_description = HTMLField(blank=False, null=False, max_length=1500)
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ads:ad_detail', kwargs={'pk': self.pk, 'slug': self.slug})
