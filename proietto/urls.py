"""proietto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user.views import EditProfileView,  ProfileView

urlpatterns = [
    path('admin/admin', admin.site.urls),

    path("user/", include("user.urls")),
    path("<slug:slug>", ProfileView.as_view(), name='profile'),
    path("<slug:slug>/edit_profile/", EditProfileView.as_view(), name='edit_profile'),


    path('', include('web.urls')),
    path('', include('ads.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
