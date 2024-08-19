# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число),
# въведени от потребителя, и пресмята и отпечатва колко струва съответното количество
# от избрания продукт в посочения град.

product = input()
city = input()
quantity = float(input())

check = 0

if city == 'Sofia':
    if product == 'coffee':
        check = quantity * 0.50
    elif product == 'water':
        check = quantity * 0.80
    elif product == 'beer':
        check = quantity * 1.20
    elif product == 'sweets':
        check = quantity * 1.45
    elif product == 'peanuts':
        check = quantity * 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        check = quantity * 0.40
    elif product == 'water':
        check = quantity * 0.70
    elif product == 'beer':
        check = quantity * 1.15
    elif product == 'sweets':
        check = quantity * 1.30
    elif product == 'peanuts':
        check = quantity * 1.50

elif city == 'Varna':
    if product == 'coffee':
        check = quantity * 0.45
    elif product == 'water':
        check = quantity * 0.70
    elif product == 'beer':
        check = quantity * 1.10
    elif product == 'sweets':
        check = quantity * 1.35
    elif product == 'peanuts':
        check = quantity * 1.55

print(check)