from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView

from user.forms.registerform import RegisterForm
from user.models import Profile


class RegisterView(CreateView):
    template_name = "auth/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        messages.success(request=self.request, message="Your account is created!")
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse("index")


class LoginView(View):
    template_name = "auth/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("index")

        return render(request, self.template_name, {})

    def post(self, request):
        username: str = request.POST.get("username")
        password: str = request.POST.get("password")

        user: User or None = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request=self.request, message="Hi! You are login.")
            return redirect("index")
        messages.warning(request=self.request, message="Wrong username or password!")
        return redirect("login")


def logout_view(request):
    logout(request)
    messages.success(request, message="Successfully logged out")
    return redirect("index")


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'

