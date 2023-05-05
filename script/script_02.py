# Создать скрипт, который принимает
# имя фамилию и возраст и дописывает их в файл
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    '-fn',
    '--first_name',
    required=True
)
parser.add_argument(
    '-ln',
    '--last_name',
    required=True
)
parser.add_argument(
    '-a',
    '--age',
    required=True
)
args = parser.parse_args()
my_list = [
    'First name:', args.first_name,
    'Last name:', args.last_name,
    'age:', args.age
]
print(*my_list)

with open('test.txt', 'a') as file:
    file.write(f'{args.first_name} {args.last_name} {args.age}\n')
