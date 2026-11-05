from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth import login
from rest_framework.exceptions import ValidationError

from users.models import CustomUser

from .forms import CustomUserCreationForm
from .services import update_bodyfat, update_lean_body_mass, update_weight_class
from django.contrib import messages

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

class CalculateBodyFatView(LoginRequiredMixin, View):

    def post(self, request):
        try:
            body_fat = update_bodyfat(request.user)
        except ValidationError as e:
            messages.error(request, str(e))
        else:
            messages.success(request, f"Процент жира: {body_fat}")
        return redirect("calculators")

class CalculateLBMView(LoginRequiredMixin, View):

    def post(self, request):
        try:
            lbm = update_lean_body_mass(request.user)
        except ValidationError as e:
            messages.error(request, str(e))
        else:
            messages.success(request, f"Обезжиренная масса тела : {lbm}")
        return redirect("calculators")

class CalculateWeightClassView(LoginRequiredMixin, View):

    def post(self, request):
        try:
            weight_class = update_weight_class(request.user)
        except ValidationError as e:
            messages.error(request, str(e))
        else:
            messages.success(request, f"Весовая категория: {weight_class}")
        return redirect("calculators")