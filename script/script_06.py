# Написать скрипт - таймер.
# Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя оставшееся время.
# Программа должна хранить файл логирования с информацией о том кто запускал программу и когда.
import os
import argparse
import time
from datetime import timedelta
import csv
from prettytable import PrettyTable


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-hr', '--hours', type=int, default=0)
parser.add_argument('-m', '--minutes', type=int, default=0)
parser.add_argument('-s', '--seconds', type=int, default=5)
args = parser.parse_args()
delta = timedelta(
    hours=args.hours,
    minutes=args.minutes,
    seconds=args.seconds
)
my_table = PrettyTable()
if not os.path.exists('log_data.csv'):
    with open('log_data.csv', 'w') as file:
        my_table.field_names = ["name", "family", "start"]
        data = my_table.get_string()
        file.write(data)

with open('log_data.csv', 'a') as file:
    # writer = csv.writer(file)
    # data = [args.first_name, args.last_name, time.ctime()]
    # writer.writerow(data)
    my_table.add_row([args.first_name, args.last_name, time.ctime()])
    data = my_table.get_string()
    file.write(data)
# не получилось разобраться как дописывать в файл, через библиотеку PrettyTable
while delta >= timedelta(seconds=0):
    print(delta)
    delta -= timedelta(seconds=1)
    time.sleep(1)
print('Finish. Go to relax')

