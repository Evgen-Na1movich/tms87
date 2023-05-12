"""
Дан список чисел. Посчитать сколько раз встречается каждое число.
Использовать функцию.
"""


def quantity_numbers(*args):
    from collections import Counter
    my_dict = {}
    for i in range(len(args)):
        my_dict[i] = args[i]
    values = my_dict.values()
    counter = Counter(values)
    return print(dict(counter))


quantity_numbers(2, 2, 4, 5, 5, 5, 3, 4)
