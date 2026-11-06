from django import forms

class NutritionSummaryForm(forms.Form):
    steps = forms.IntegerField(min_value=0, label="Количество шагов за день: ")
    train_time = forms.IntegerField(min_value=0, label="Количество минут тренировки за день: ")
    goal = forms.ChoiceField(choices=[("low", "медленно"),("medium", "средне"),("agressive", "быстро")],
                             initial="medium",
                             required=False)