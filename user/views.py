from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


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
    messages.success(request, message="Successfully loged out")
    return redirect("index")
