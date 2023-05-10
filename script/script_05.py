# Создать скрипт. Программа принимает имя папки и имя файла с расширением.
# Создает папку и создает в ней файл.
# Если расширение файла py - записывает в файл следующее:
# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()
import argparse
import os
from os import path

parser = argparse.ArgumentParser()
parser.add_argument(
    '-dn',
    '--dir_name',
    type=str,
    required=True
)
parser.add_argument(
    '-fn',
    '--file_name',
    type=str,
    required=True
)
args = parser.parse_args()
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)
with open(os.path.join(args.dir_name, args.file_name), 'w') as file:
    file.write("")

name_file = path.splitext(args.file_name)[-1]
# name_file = os.path.basename(os.path.realpath(__file__))
if name_file == '.py':
    with open(os.path.join(args.dir_name, args.file_name), 'w') as file:
        file.write(""
                   "def main():\n"
                   "    pass\n"
                   "\n"
                   "\n"
                   "if __name__ == 'main':\n"
                   "    main()\n"
                   )

