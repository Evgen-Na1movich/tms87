import csv
import os
import argparse
import time
from datetime import timedelta

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-hr', '--hours', default=0, type=int)
parser.add_argument('-m', '--minutes', default=0, type=int)
parser.add_argument('-s', '--seconds', default=5, type=int)
parser.add_argument('-tom', '--time_out_minutes', default=0, type=int)
parser.add_argument('-tos', '--time_out_seconds', default=1, type=int)
parser.add_argument('-nc', '--numbers_cycles', default=3, type=int)
parser.add_argument('-nt', '--name_task')
args = parser.parse_args()

time_work = timedelta(
    hours=args.hours,
    minutes=args.minutes,
    seconds=args.seconds
)
time_out = timedelta(
    hours=0,
    minutes=args.time_out_minutes,
    seconds=args.time_out_seconds
)

if not os.path.exists('log_timer.csv'):
    with open('log_timer.csv', 'w') as file:
        writer = csv.writer(file)
        data = ["name", "family", "start", 'name task']
        writer.writerow(data)

with open('log_timer.csv', 'a') as file:
    writer = csv.writer(file)
    data = [args.first_name, args.last_name, time.ctime(), args.name_task]
    writer.writerow(data)

# all_time = time_work * args.numbers_cycles + time_out * (args.numbers_cycles - 1)
# time_task = timedelta(seconds=0)
# time_relax = timedelta(seconds=0)


# while all_time > timedelta(seconds=0):
#     if time_task == time_work:
#         print('Go to relax!')
#         time_task = timedelta(seconds=0)
#     elif time_relax == time_work + time_out:
#         print("The break is over. Let's work!")
#         time_relax = timedelta(seconds=0)
#         time_task = timedelta(seconds=0)
#     if time_task == time_relax:
#         print(time_work - time_task)
#     else:
#         print(time_out - time_task)
#     time_task += timedelta(seconds=1)
#     time_relax += timedelta(seconds=1)
#     all_time -= timedelta(seconds=1)
#     time.sleep(1)
# os.system('cls')
# print('Finish!')


def timer(name: str, time_o: timedelta):
    print(f'start {name}')
    while time_o:
        print(f'{time_o}')
        time_o -= timedelta(seconds=1)
        time.sleep(1)


for i in range(1, args.numbers_cycles + 1):
    print(f'Start of the cycle {i}')
    if args.numbers_cycles > 1:
        timer('task_07', time_work)
        timer('relax', time_out)
        args.numbers_cycles -= 1
    else:
        timer('task_07', time_work)
print("Finish")
