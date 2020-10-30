from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Created(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Ad(Created):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
