"""
Написать программу для нахождения факториала. Факториал натурального
числа n определяется как произведение всех натуральных чисел от 1 до n включительно
"""


def factorial(number: int):
    res = 1
    for i in range(1, number + 1):
        res *= i
    return res


print(factorial(5))
