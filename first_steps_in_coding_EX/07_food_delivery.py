# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
#     • Пилешко меню –  10.35 лв.
#     • Меню с риба – 12.40 лв.
#     • Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

chicken_menues = int(input())
fish_menues = int(input())
vegie_menues = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegie_menu_price = 8.15
desert_price = 20/100
delivery = 2.50

chicken_total_price = chicken_menues * chicken_menu_price
fish_total_price = fish_menues * fish_menu_price
vegie_total_price = vegie_menues * vegie_menu_price

total_menues_price = chicken_total_price + fish_total_price + vegie_total_price
price_with_desert = (total_menues_price * desert_price) + total_menues_price

total_order_price = price_with_desert + delivery

print(total_order_price)