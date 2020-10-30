from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField

class Ad(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False, unique=False)
    image = models.ImageField(blank=False, null=False, upload_to='ads_image/')
    body = body = HTMLField(max_length=1000, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):  # opisać tą funckję
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Ads'