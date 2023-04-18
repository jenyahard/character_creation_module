from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(numerical_value):
    """Вычисляет квадратный корень."""
    return sqrt(numerical_value)


def calc(numerical_value):
    """Вычисляет квадратный корень."""
    if numerical_value >= 0:
        result = calculate_square_root(numerical_value)
        return print(f'Мы вычислили квадратный корень из введённого вами '
                     f'числа. Это будет:{result}')


calc(25.5)
