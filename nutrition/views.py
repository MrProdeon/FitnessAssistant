from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from nutrition.forms import NutritionSummaryForm
from nutrition.services import calculate_nutrition_summary

class NutritionSummaryView(LoginRequiredMixin, View):


    def post(self, request):
        form = NutritionSummaryForm(request.POST)

        if form.is_valid():
            steps = form.cleaned_data["steps"]
            train_time = form.cleaned_data["train_time"]
            goal = form.cleaned_data["goal"] or "medium"
            calculate_nutrition_summary(request.user, steps, train_time, goal)
            return redirect("nutrition-calculators")