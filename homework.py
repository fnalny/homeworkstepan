class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type #имя класса тренировки
        self.duration = duration #длительность тренировки в часах
        self.distance = distance #дистанция в километрах, которую преодолел пользователь за время тренировки
        self.speed = speed # средняя скорость, с которой двигался пользователь
        self.calories = calories # количество килокалорий, которое израсходовал пользователь за время тренировки


    def get_message(self):
        return (f'Тип тренировки: {training_type}; '
                'Длительность: {duration}:.3f ч.; '
                'Дистанция: {distance}:.3f км;')
    

    def show_training_info():


class Training:
    """Базовый класс тренировки."""

M_IN_KM = 1000


    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return (self.action * self.LEN_STEP / self.M_IN_KM) # Возвращает дистанцию (в километрах), которую преодолел пользователь за время тренировки

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.get_distance / self.duration) #Возвращает значение средней скорости движения во время тренировки

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass #Так и оставляем. Возвращает количество килокалорий, израсходованных за время тренировки

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return() #возвращает объект класса сообщения


class Running(Training):
    """Тренировка: бег."""
LEN_STEP = 0.65
CALORIES_MEAN_SPEED_MULTIPLIER = 18
CALORIES_MEAN_SPEED_SHIFT = 1.79


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
LEN_STEP = 0.65
    pass



class Swimming(Training):
    """Тренировка: плавание."""
LEN_STEP = 1.38
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

