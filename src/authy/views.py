from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginPageForm, RegisterPageForm


class RegisterPageView(SuccessMessageMixin, CreateView):
    template_name = 'authy/register.html'
    form_class = RegisterPageForm
    success_url = reverse_lazy('authy:register')
    success_message = "Has sido registrado exitosamente"


class LoginPageView(LoginView):
    template_name = 'authy/login.html'
    authentication_form = LoginPageForm
    redirect_authenticated_user = 'crud:home'


class LogoutPageView(LogoutView):
    pattern_name = 'authy:login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)








