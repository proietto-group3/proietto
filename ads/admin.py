from django.contrib import admin

from ads.models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_on', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Ad, AdAdmin)