# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.
# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
#     • Първият ред съдържа час на изпита - цяло число от 0 до 23;
#     • Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
#     • Третият ред съдържа час на пристигане - цяло число от 0 до 23;
#     • Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
# Изход
# На първия ред отпечатайте:
#     • "Late", ако студентът пристига по-късно от часа на изпита;
#     • "On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
#     • "Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
#     • "mm minutes before the start" за идване по-рано с по-малко от час;
#     • "hh:mm hours before the start" за подраняване с 1 час или повече.
#     Минутите винаги печатайте с 2 цифри, например "1:05”;
#     •  "mm minutes after the start" за закъснение под час;
#     • "hh:mm hours after the start" за закъснение от 1 час или повече.
#     Минутите винаги печатайте с 2 цифри, например "1:03

from math import fabs

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_minutes = (exam_hour * 60) + exam_minutes
total_arrival_minutes = (arrival_hour * 60) + arrival_minutes

difference_between_time = total_minutes - total_arrival_minutes

new_hours = difference_between_time / 60
new_minutes = difference_between_time % 60

if exam_minutes < arrival_minutes:
    print('Late')
    if new_hours >= 1:
        if new_minutes < 10:
            print(f"{new_hours}:0{new_minutes} hours after the start")
        else:
            print(f"{new_hours}:{new_minutes} hours after the start")
    else:
        print(f"{new_minutes} minutes after the start")

elif exam_minutes - arrival_minutes <= 30:
    print('On time')
    if exam_minutes != arrival_minutes:
        print(f"{fabs(difference_between_time)} minutes before the start")
elif exam_minutes - arrival_minutes > 30:
    if exam_minutes > arrival_minutes:
        print('Early')
    difference_between_time = exam_minutes - arrival_minutes
    new_hours = fabs(new_hours)
    new_minutes = fabs(new_minutes)
    if new_hours >= 1:
        if new_minutes < 10:
            print(f"{new_hours}:0{new_minutes} hours before the start")
        else:
            print(f"{new_hours}:{new_minutes} hours before the start")
    else:
        print(f"{new_minutes} minutes before the start")
