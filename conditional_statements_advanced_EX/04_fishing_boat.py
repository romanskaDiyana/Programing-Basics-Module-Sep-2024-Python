# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
#     • Цената за наем на кораба през пролетта е  3000 лв.;
#     • Цената за наем на кораба през лятото и есента е  4200 лв.;
#     • Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
#     • Ако групата е до 6 човека включително  -  отстъпка от 10%;
#     • Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
#     • Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен -
# тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

group_budget = int(input())
season = input()
fishermen_count = int(input())

ship_price = 0

spring_price = 3000
summer_price = 4200
autumn_price = 4200
winter_price = 2600

if season == 'Spring':
    if fishermen_count <= 6:
        ship_price = spring_price - (spring_price * 0.10)
    elif fishermen_count >=7 and fishermen_count <= 11:
        ship_price = spring_price - (spring_price * 0.15)
    elif fishermen_count >= 12:
        ship_price = spring_price - (spring_price * 0.25)

    if fishermen_count % 2 == 0:
        ship_price = ship_price - (ship_price * 0.05)
elif season == 'Summer':
    if fishermen_count <= 6:
        ship_price = summer_price - (summer_price * 0.10)
    elif fishermen_count >= 7 and fishermen_count <= 11:
        ship_price = summer_price - (summer_price * 0.15)
    elif fishermen_count >= 12:
        ship_price = summer_price - (summer_price * 0.25)

    if fishermen_count % 2 == 0:
        ship_price = ship_price - (ship_price * 0.05)
elif season == 'Autumn':
    if fishermen_count <= 6:
        ship_price = autumn_price - (autumn_price * 0.10)
    elif fishermen_count >= 7 and fishermen_count <= 11:
        ship_price = autumn_price - (autumn_price * 0.15)
    elif fishermen_count >= 12:
        ship_price = autumn_price - (autumn_price * 0.25)
elif season == 'Winter':
    if fishermen_count <= 6:
        ship_price = winter_price - (winter_price * 0.10)
    elif fishermen_count >= 7 and fishermen_count <= 11:
        ship_price = winter_price - (winter_price * 0.15)
    elif fishermen_count >= 12:
        ship_price = winter_price - (winter_price * 0.25)

    if fishermen_count % 2 == 0:
        ship_price = ship_price - (ship_price * 0.05)

if ship_price <= group_budget:
    print(f"Yes! You have {group_budget - ship_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {ship_price - group_budget:.2f} leva.")