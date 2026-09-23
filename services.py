from rest_framework.exceptions import ValidationError

from users.models import CustomUser
from math import log10

def get_required_fields(user: CustomUser) -> tuple[str, ...]:
    if user.sex == CustomUser.Sex.MALE:
        return "age", "weight", "height", "neck", "waist"
    elif user.sex == CustomUser.Sex.FEMALE:
        return "age", "weight", "height", "neck", "waist", "hip"
    raise ValueError("Пол не указан или неизвестен")

def validate_body_fat_fields(user: CustomUser) -> None:
    missing = [f for f in get_required_fields(user) if getattr(user, f, None) in (None, "")]
    if missing:
        raise ValidationError(f"Пропущены обязательные поля: {', '.join(missing)}")


def calculate_body_fat(user: CustomUser) -> float:

    validate_body_fat_fields(user)

    if user.sex == CustomUser.Sex.MALE:
        inner = 1.0324 - 0.19077 * log10(user.waist - user.neck) + 0.15456 * log10(user.height)
    else:
        inner = 1.29579 - 0.35004 * log10(user.waist + user.hip - user.neck) + 0.22100 * log10(user.height)

    return 495 / inner - 450

if __name__ == "__main__":
    print(validate_body_fat_fields(CustomUser.objects.filter(pk=3)))
