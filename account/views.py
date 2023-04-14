from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from account.forms import CustomAuthenticationForm, UserRegistrationForm
from account.models import User
from django.views.generic import DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"


def custom_login(request):
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password:
            user = authenticate(
                request, username=username, password=password
            )
            login(request, user)
            user.save()
            return redirect("account:profile")
    return render(request, "account/login.html", {"form": form})


class UserProfile(DetailView, LoginRequiredMixin):
    model = User
    pk_url_kwarg = None
    query_pk_and_slug = None

    def get_queryset(self):
        return self.request.user


@login_required
def profile(request):
    return render(request, "account/profile.html", {"user": request.user})


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("account:login")

    # def post(self, request):
    #     form = UserRegistrationForm(request.POST or None)
    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         first_name = form.cleaned_data.get("first_name")
    #         last_name = form.cleaned_data.get("last_name")
    #         email = form.cleaned_data.get("email")
    #         password = form.cleaned_data.get("password")
    #         User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    #         return redirect("homepage")
    #     return render(request, "account/register.html", {"form": form})
