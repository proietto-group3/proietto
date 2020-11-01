from django.contrib import admin

from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'account_type', 'date_joined')
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(Profile, ProfileAdmin)
