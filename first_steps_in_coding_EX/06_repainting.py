# Румен иска да пребоядиса хола и за целта е наел майстори.
# Напишете програма, която изчислява разходите за ремонта, предвид следните цени:
#     • Предпазен найлон - 1.50 лв. за кв. метър
#     • Боя - 14.50 лв. за литър
#     • Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали,
# Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон,
# разбира се и 0.40 лв. за торбички.
# Сумата, която се заплаща на майсторите за 1 час работа,
# е равна на 30% от сбора на всички разходи за материали.

needed_amount_of_nylon = int(input())
needed_amount_of_paint = int(input())
needed_amount_of_thinner = int(input())
hours_work = int(input())

price_for_nylon = 1.50
price_for_paint = 14.50
extra_paint = 10/100
thinner = 5.00
bags = 0.40

nylon_quantity = (needed_amount_of_nylon + 2) * price_for_nylon
paint_quantity = (needed_amount_of_paint * price_for_paint * extra_paint) + needed_amount_of_paint * price_for_paint
thinner_quantity = needed_amount_of_thinner * thinner

total_summury = nylon_quantity + paint_quantity + thinner_quantity + bags
total_price = ((total_summury * 0.30) * hours_work) + total_summury

print(total_price)