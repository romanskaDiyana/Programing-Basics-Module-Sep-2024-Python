# Напишете програма, която пресмята колко общо пари има в сметката,
# след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката,
# до получаване на команда  "NoMoreMoney ".
# При всяка получена сума на конзолата трябва да се извежда
# "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"
# и програмата да приключи. Когато програмата приключи трябва да се принтира
# "Total: " + общата сума в сметката форматирана до втория знак след десетичната запетая.

imported_money = input()

total_money = 0

while imported_money != 'NoMoreMoney':
    imported_money = float(imported_money)

    if imported_money < 0:
        print('Invalid operation!')
        break

    total_money += imported_money
    print(f'Increase: {imported_money:.2f}')

    imported_money = input()


print(f'Total: {total_money:.2f}')