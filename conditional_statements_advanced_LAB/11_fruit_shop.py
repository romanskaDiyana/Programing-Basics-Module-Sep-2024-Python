# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
#     • плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
#     • ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
#     • количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата
# или невалидно име на плод да се отпечата "error".

fruit = input()
day_of_week = input()
quantity = float(input())

price = 0
ERROR_DATA = False

if fruit == 'banana':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 2.50
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 2.70
    else:
        ERROR_DATA = True
elif fruit == 'apple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 1.20
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 1.25
    else:
        ERROR_DATA = True
elif fruit == 'orange':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 0.85
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 0.90
    else:
        ERROR_DATA = True
elif fruit == 'grapefruit':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 1.45
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 1.60
    else:
        ERROR_DATA = True
elif fruit == 'kiwi':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 2.70
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 3.00
    else:
        ERROR_DATA = True
elif fruit == 'pineapple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 5.50
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 5.60
    else:
        ERROR_DATA = True
elif fruit == 'grapes':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 3.85
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 4.20
    else:
        ERROR_DATA = True
else:
    ERROR_DATA = True

if ERROR_DATA:
    print('error')
else:
    print(f'{price:.2f}')