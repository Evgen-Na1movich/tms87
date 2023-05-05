# Создать скрипт.
# Программа принимает имя папки и имя файла.
# Создает папку и создает в ней файл.
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-dn',
    '--dir_name',
    required=True
)
parser.add_argument(
    '-fn',
    '--file_name',
    required=True
)
args = parser.parse_args()
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)
with open(os.path.join(args.dir_name, args.file_name), 'w') as file:
    # file.write("")
    pass



