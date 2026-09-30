from users.models import CustomUser


def calculate_bmr(user: CustomUser):
    """
    Калькулятор базового обмена веществ. Для расчета используется обезжиренная масса тела пользователя.
    :param user: Пользователь
    :return: Базовый обмен веществ пользователя
    """
    bmr = 370 + (21.6 * user.lean_body_mass)

    #Добавить запись в бд
    return bmr

def calculate_calorie_norm(user: CustomUser):
    pass

def calculate_protein_norm(user: CustomUser):
    """
    Рассчет нормы потребляемого белка в день для быстрого жиросжигания
    :param user: Пользователь
    :return: норма потребляемого белка в день
    """
    if user.weight_class == CustomUser.WeightClass.SLENDER:
        protein_norm = 4.4 * user.lean_body_mass
    elif user.weight_class == CustomUser.WeightClass.EXCESS_WEIGHT:
        protein_norm = 2.75 * user.lean_body_mass
    else:
        protein_norm = 2.2 * user.lean_body_mass

    #Добавить запись в бд
    return protein_norm

def calculate_fat_norm(calorie_norm: float) -> float:
    """
    Рассчет нормы потребляемого жира в день для быстрого жиросжигания
    :param calorie_norm: норма потребляемых калорий пользователя
    :return: норма потребляемого жира в день
    """
    # Необходимо 2 грамма омега 3 в день, остальное возьмется из подкожного жира
    fat_norm = calorie_norm * 0.3 / 9
    return fat_norm