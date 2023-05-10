"""
Создать функцию, которая принимает на вход
неопределенное количество именованных аргументов
 и выводит на экран те из них, длина ключа которых четна.
 """


def return_key_even_len(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if not len(key) % 2:
            my_dict[key] = value
    return my_dict


print(return_key_even_len(name="Evgen", age=34, city="Minsk"))
