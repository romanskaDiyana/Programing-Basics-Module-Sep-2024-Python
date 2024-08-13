# Учебната година вече е започнала и отговорничката на 10Б клас -
# Ани трябва да купи определен брой пакетчета с химикали, пакетчета с маркери,
# както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница,
# затова има намаление за нея, което представлява някакъв процент от общата сума.
# Напишете програма, която изчислява колко пари ще трябва да събере Ани,
# за да плати сметката, като имате предвид следния ценоразпис:
#     • Пакет химикали - 5.80 лв.
#     • Пакет маркери - 7.20 лв.
#     • Препарат - 1.20 лв (за литър)

number_of_pens = int(input())
number_of_markers = int(input())
liters_of_cleaning_product = int(input())
discount_procent = int(input())

price_of_pens = 5.80
price_of_markers = 7.20
price_per_cleaning_product = 1.20

total_price = (number_of_pens * price_of_pens
              + number_of_markers * price_of_markers
              + liters_of_cleaning_product * price_per_cleaning_product)

total_price_after_discount = total_price - (total_price * (discount_procent / 100))

print(total_price_after_discount)
