# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой
# за студио и апартамент. Цените зависят от месеца на престоя:
# Предлагат се и следните отстъпки:
#     • За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#     • За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#     • За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#     • За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
#     • На първия ред е месецът - May, June, July, August, September или October;
#     • На втория ред е броят на нощувките - цяло число.
# Изход
# Да се отпечатат на конзолата 2 реда:
#     • На първия ред: "Apartment: {цена за целият престой} lv."
#     • На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.

month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    if nights_count > 14:
        studio_price = nights_count * 50 - ((nights_count * 50) * 0.30)
        apartment_price = nights_count * 65 - ((nights_count * 65) * 0.10)
    elif nights_count > 7:
        studio_price = nights_count * 50 - ((nights_count * 50) * 0.05)
        apartment_price = nights_count * 65
    else:
        studio_price = nights_count * 50
        apartment_price = nights_count * 65
elif month == 'June' or month == 'September':
    if nights_count > 14:
        studio_price = nights_count * 75.20 - ((nights_count * 75.20) * 0.20)
        apartment_price = nights_count * 68.70 - ((nights_count * 68.70) * 0.10)
    else:
        studio_price = nights_count * 75.20
        apartment_price = nights_count * 68.70
elif month == 'July' or month == 'August':
    if nights_count > 14:
        apartment_price = nights_count * 77 - ((nights_count * 77) * 0.10)
        studio_price = nights_count * 76
    else:
        studio_price = nights_count * 76
        apartment_price = nights_count * 77

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")