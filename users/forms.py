from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser

# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["email",  "phone_number", "age",
                  "weight", "height", "neck", "waist",
                  "sex", "hip"]
        labels = {
            "email": "Электронная почта",
            "phone_number": "Номер телефона",
            "age": "Возраст",
            "sex": "Пол",
            "weight": "Вес (кг)",
            "height": "Рост (см)",
            "neck": "Обхват шеи (см)",
            "waist": "Обхват талии (см)",
            "hip": "Обхват бёдер (см)",
        }
        help_texts = {
            "email": "Будет использоваться для входа в аккаунт.",
            "age": "Полных лет. Нужен для расчёта обмена веществ.",
            "weight": "Текущий вес в килограммах. Нужен для расчёта калорий и нормы белка.",
            "height": "Рост в сантиметрах.",
            "neck": "Измеряется под гортанью, лента горизонтально. Нужен для расчёта процента жира.",
            "waist": "Для мужчин измеряется на уровне пупка, для женщин в самом узком месте. Нужен для расчёта процента жира.",
            "hip": "Измеряется по самой широкой части. Нужен только женщинам для расчёта процента жира.",
            "sex": "Нужен для точности измерений."
        }

# Форма авторизации
class CustomAuthenticationForm(AuthenticationForm):
    pass