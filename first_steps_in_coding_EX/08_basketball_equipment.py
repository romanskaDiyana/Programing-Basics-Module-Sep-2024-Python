# Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка.
# Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира,
# като знаете колко е таксата за тренировки по баскетбол за период от 1 година. Нужна екипировка:
#     • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#     • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#     • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#     • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

tax_per_year_for_training = int(input())

sneakers_price = tax_per_year_for_training * ((100-40) / 100)
outfit_price = sneakers_price - (sneakers_price * 0.20)
ball_price = outfit_price / 4
accessories_price = ball_price / 5

total_price_for_equipment = sneakers_price + outfit_price + ball_price + accessories_price + tax_per_year_for_training

print(total_price_for_equipment)

