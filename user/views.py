from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin as BaseLoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, FormView

from user.forms.editprofileform import EditProfileForm
from user.forms.registerform import RegisterForm
from user.models import Profile


class LoginRequiredMixin(BaseLoginRequiredMixin):
    def get_login_url(self):
        return reverse("user:login")


class RegisterView(CreateView):
    template_name = "auth/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        messages.success(request=self.request, message="Your account is created! You can login.")
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
        return redirect("user:login")


def logout_view(request):
    logout(request)
    messages.success(request, message="Successfully logged out")
    return redirect("index")


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'profile/edit_profile.html'
    form_class = EditProfileForm

    def get_success_url(self):
        slug = self.kwargs['slug']
        messages.success(request=self.request, message="Profile updated")
        return reverse_lazy("profile", kwargs={'slug': slug})

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        # todo: DOROBIĆ MESSAGES LUB template/html JEŚLI PROBUJE SIĘ EDYTOWAC OBCY PROFIL
        return False


class ChangePassword(LoginRequiredMixin, FormView):
    login_url = "/login"
    template_name = "auth/change_password.html"
    form_class = PasswordChangeForm

    def get_form(self):
        if self.request.POST:
            return self.form_class(self.request.user, self.request.POST)
        return self.form_class(self.request.user)

    def form_valid(self, form):
        messages.success(request=self.request, message="Password has been changed. You can login with new password.")
        form.save()
        return redirect(reverse('user:login'))

    def get_success_url(self) -> str:
        return reverse("user:login")
