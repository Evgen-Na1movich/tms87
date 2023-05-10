# Создать скрипт, который принимает имя папки
# и создает ее рядом со скриптом
import os
import argparse

file_path = os.path.realpath(__file__)
print(file_path)
dir_name = os.path.dirname(file_path)
print(dir_name)

parser = argparse.ArgumentParser()
parser.add_argument(
    '-dn',
    '--dir_name',
    required=True
)
args = parser.parse_args()
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)
