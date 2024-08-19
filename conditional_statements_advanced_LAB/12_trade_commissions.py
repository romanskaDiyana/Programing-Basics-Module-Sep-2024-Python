# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица. Резултатът да се изведе форматиран до
# 2 цифри след десетичната точка. При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

city = input()
sales = float(input())

commission = 0.0
ERROR_DATA = False

if city == 'Sofia':
    if sales >= 0 and sales <= 500:
        commission = (sales * (5 / 100 + 1)) - sales
    elif sales > 500 and sales <= 1000:
        commission = (sales * (7 / 100 + 1)) - sales
    elif sales > 1000 and sales <= 10000:
        commission = (sales * (8 / 100 + 1)) - sales
    elif sales > 10000:
        commission = (sales * (12 / 100 + 1)) - sales
    else:
        ERROR_DATA = True
elif city == 'Varna':
    if sales >= 0 and sales <= 500:
            commission = (sales * (4.5 / 100 + 1)) - sales
    elif sales > 500 and sales <= 1000:\
        commission = (sales * (7.5 / 100 + 1)) - sales
    elif sales > 1000 and sales <= 10000:
        commission = (sales * (10 / 100 + 1)) - sales
    elif sales > 10000:
        commission = (sales * (13 / 100 + 1)) - sales
    else:
        ERROR_DATA = True
elif city == 'Plovdiv':
        if sales >= 0 and sales <= 500:
            commission = (sales * (5.5 / 100 + 1)) - sales
        elif sales > 500 and sales <= 1000:
            commission = (sales * (8 / 100 + 1)) - sales
        elif sales > 1000 and sales <= 10000:
            commission = (sales * (12 / 100 + 1)) - sales
        elif sales > 10000:
            commission = (sales * (14.5 / 100 + 1)) - sales
        else:
            ERROR_DATA = True
else:
    ERROR_DATA = True

if ERROR_DATA:
    print('error')
else:
    print(f'{commission:.2f}')