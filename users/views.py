from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import modelform_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login
from users.models import CustomUser

from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class Login(LoginView):
    template_name = "users/login.html"

class CustomUserEditView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("home")
    success_message = "Данные изменены"

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_class(self):
        field = self.kwargs["field"]
        if field not in CustomUser.PROFILE_FIELDS:
            raise Http404
        return modelform_factory(CustomUser, fields=[field])