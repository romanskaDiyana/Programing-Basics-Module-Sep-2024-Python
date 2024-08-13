# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма,
# която да изчисли, дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
#         ◦ Декорът за филма е на стойност 10% от бюджета.
#         ◦ При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

film_budget = float(input())
actors_count = int(input())
price_for_outfit_for_one_actor = float(input())

price_for_decor = film_budget * 0.10
price_for_outfit = price_for_outfit_for_one_actor * actors_count

if actors_count > 150:
    price_for_outfit = price_for_outfit - (price_for_outfit * 0.10)

total_price = price_for_outfit + price_for_decor

if total_price <= film_budget:
    print('Action!')
    print(f'Wingard starts filming with {film_budget - total_price:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {total_price - film_budget:.2f} leva more.')