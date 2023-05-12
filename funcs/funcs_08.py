"""
Написать функцию принимающая на вход неопределенным количеством аргументов
и именованный аргумент mean_type. В зависимости от mean_type вернуть
среднеарифметическое либо среднегеометрическое. Написать программу в виде трех функций.
"""


def avg_arithmetic(*args):
    return sum(args) / len(args)


def avg_geometric(*args):
    from functools import reduce
    product_of_numbers = reduce((lambda x, y: x * y), args, 1)
    return product_of_numbers ** (1 / len(args))


def avg_type(*args, mean_type):
    if mean_type == 0:
        return print(avg_arithmetic(*args))
    else:
        return print(avg_geometric(*args))


print(avg_arithmetic(3, 3, 3, 4, 5, 6, ))
print(avg_geometric(3, 3, 3, 4, 5, 6))
avg_type(3, 3, 3, 4, 5, 6, mean_type=0)
avg_type(3, 3, 3, 4, 5, 6, mean_type=1)
