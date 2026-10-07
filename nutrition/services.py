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

def calculate_tef(bmr : float | int, ) -> int | float:
    """
    Рассчет калорий, которые уходят на перевание пищи. Учитываем консервативно всего 10%.
    На деле может разниться от 10% до 20% в зависимости от количества потребления белка и клетчатки
    :param bmr: базовый обмен веществ пользователя
    :return: траты на переваривение пищи
    """
    return bmr * 0.10

def calculate_calories_per_1000_steps(user : CustomUser) -> int | float:
    """
    Примерный расчет трат калорий на 1000 шагов
    :param user: Пользователь
    :return: количество калорий, потраченных на 1000 шагов
    """
    return user.weight * 0.5

def calculate_calories_by_steps(user : CustomUser, steps : int) -> int | float:
    """
    Рассчет калорий, потраченных на шаги
    :param user: Пользователь
    :param steps: Количество пройденных шагов
    :return: количество калорий, потраченных на указанное количество шагов
    """
    return calculate_calories_per_1000_steps(user) * (steps / 1000)

def calculate_neat(user: CustomUser, steps: int | float) -> int | float:
    """
    Рассчет трат калорий в день без тренировки. Учитывается базовый обмен веществ, шаги и траты на переваривание пищи.
    :param user: Пользователь
    :param steps: Количество шагов в день
    :return: Траты калорий в день без тренировки
    """
    bmr = calculate_bmr(user)
    steps = calculate_calories_by_steps(user, steps)
    tef = calculate_tef(bmr)

    return bmr + steps + tef

def calculate_train_calorie(user: CustomUser, train_time : int) -> int | float:
    """
    Рассчет трат калорий за тренировку, с учётом уровня физическое подготовки
    :param user: Пользователь
    :param train_time: Время тренировки
    :return: Калории, потраченные за тренировку
    """
    if user.fitness_level == CustomUser.FitnessLevel.LOW:
        coefficient = 0.05
    elif user.fitness_level == CustomUser.FitnessLevel.MEDIUM:
        coefficient = 0.75
    else:
        coefficient = 0.1

    train_calories = coefficient * user.weight * train_time

    return train_calories

def calculate_eat():
    pass

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

def calculate_nutrition_summary(user: CustomUser):
    calorie_norm = calculate_calorie_norm(user)
    return {
        "bmr" : calculate_bmr(user),
        "calorie_norm" : calorie_norm,
        "protein_norm" : calculate_protein_norm(user),
        "fat_norm" : calculate_fat_norm(calorie_norm)
    }