"""
Создать функцию, принимающая на вход неопределенное количество
аргументов и возвращающая сумму args[i] * i
"""


def summa_arg(*args):
    sum_res = 0
    for i in args:
        for j in range(len(i)):
            sum_res += i[j] * j
    return sum_res


my_list = [4, 3, 2, 1, 5, 7, 1]
print(summa_arg(my_list))
