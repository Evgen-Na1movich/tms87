"""
Написать функцию по решению квадратных уравнений
"""


def root_quadr_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return print('root is not')
    if d == 0:
        return print(f'root -> {-b / (2 * a)}')
    else:
        return print(f'root_1 -> {(-b - d ** 0.5) / (2 * a)},root_2 -> {(-b + d ** 0.5) / (2 * a)}')


root_quadr_equation(-4, 28, -49)
root_quadr_equation(6, 3, 0)
