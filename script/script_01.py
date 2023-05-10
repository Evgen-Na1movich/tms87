# Создать скрипт, который при запуске принимает
# неопределенное количество аргументов и
# считает сумму тех из них, что являются цифрами.
import sys

# v1
args = sys.argv
summa_args = sum([int(i) for i in args if i.isdigit()])
print(summa_args)

# v2
my_list = []
for i in args:
    if i.isdigit():
        my_list.append(int(i))
print(sum(my_list))
