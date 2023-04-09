from django.contrib.auth.views import LoginView

from account.forms import CustomAuthenticationForm


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"
    # success_url = "account/profile"
