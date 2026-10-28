from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser


# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "phone_number", "age", "sex",
                  "weight", "height", "neck", "waist", "hip"]
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
            "age": "Полных лет.",
            "weight": "Нужен для расчёта калорий и нормы белка.",
            "height": "Нужен для расчёта обмена веществ.",
            "neck": "Под гортанью, лента горизонтально. Для процента жира.",
            "waist": "Мужчины: на уровне пупка. Женщины: в самом узком месте.",
            "hip": "По самой широкой части. Нужен только женщинам.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Пароль"
        self.fields["password1"].help_text = "Минимум 8 символов, не только цифры."
        self.fields["password2"].label = "Подтверждение пароля"
        self.fields["password2"].help_text = ""
        # стили Spark для всех полей
        for field in self.fields.values():
            field.widget.attrs["class"] = "login-input"


# Форма авторизации
class CustomAuthenticationForm(AuthenticationForm):
    pass