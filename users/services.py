from rest_framework.exceptions import ValidationError

from users.models import CustomUser
from math import log10

# BODY FAT
def get_required_fields(user: CustomUser) -> tuple[str, ...]:
    """
    Определяет какие обязательные поля должны быть указаны у пользователя,
    чтобы корректно рассчитать процент жира в теле

    :param user: Пользователь
    :return: обязательные поля для расчета процента жира, исходя из пола пользователя
    """
    if user.sex == CustomUser.Sex.MALE:
        return "age", "weight", "height", "neck", "waist"
    elif user.sex == CustomUser.Sex.FEMALE:
        return "age", "weight", "height", "neck", "waist", "hip"
    raise ValueError("Пол не указан или неизвестен")

def validate_body_fat_fields(user: CustomUser) -> None:
    """
    Валидация обязательных полей для расчета процента жира. Если какого-то поля нет - вызывает исключение.
    :param user: Пользователь
    :return: None
    """
    missing = [f for f in get_required_fields(user) if getattr(user, f, None) in (None, "")]
    if missing:
        raise ValidationError(f"Пропущены обязательные поля: {', '.join(missing)}")


def calculate_body_fat(user: CustomUser) -> float:
    """
    Рассчет процента жира пользователя и сохранение данных в модель пользователя.
    Источник - https://www.calculator.net/body-fat-calculator.html
    :param user: Пользователь
    :return: процент жира в теле пользователя
    """

    validate_body_fat_fields(user)

    if user.sex == CustomUser.Sex.MALE:
        inner = 1.0324 - 0.19077 * log10(user.waist - user.neck) + 0.15456 * log10(user.height)
    else:
        inner = 1.29579 - 0.35004 * log10(user.waist + user.hip - user.neck) + 0.22100 * log10(user.height)

    body_fat = 495 / inner - 450

    user.body_fat = body_fat
    user.save(update_fields=["body_fat"])

    return body_fat


#Lean Body Mass

def get_lean_body_mass(user: CustomUser) -> float:
    """
    Рассчет обезжиренной массы тела, исходя из веса и процента жира пользователя. Сохранение в модель пользователя.
    :param user: Пользователь
    :return: обезжиренная масса тела
    """
    lean_body_mass = user.weight * (1 - user.body_fat / 100)
    user.lean_body_mass = lean_body_mass
    user.save(update_fields = ["lean_body_mass"])


    return lean_body_mass

# weight class

def get_weight_class(user: CustomUser) -> str:
    """
     Функция для определения весовой категории пользователя, исходя из процента жира
    :param user: Пользователь
    :return: весовая категория пользователя
    """
    body_fat, sex = user.body_fat, user.sex


    if sex == CustomUser.Sex.MALE:
        if body_fat <= 15:
            weight_class = "стройный"
        elif 16 <= body_fat <= 25:
            weight_class = "лишний вес"
        elif body_fat >= 26:
            weight_class = "ожирение"

    else:
        if body_fat <= 25.4:
            weight_class = "стройный"
        elif 25 <= body_fat <= 34:
            weight_class = "лишний вес"
        elif body_fat >= 35:
            weight_class = "ожирение"

    return weight_class



