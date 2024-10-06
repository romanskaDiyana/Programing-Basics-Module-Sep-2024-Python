# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее
# да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# От конзолата се четат:
#     • Пари, нужни за екскурзията - реално число;
#     • Налични пари - реално число.
# След това многократно се четат по два реда:
#     • Вид действие – текст с две възможности: "spend" или "save";
#     ◦ Сумата, която ще спести/похарчи - реално число.


money_needed = float(input())
saved_money = float(input())

following_days = 0
days_counter = 0

while following_days < 5:
    days_counter += 1
    action = input()
    money = float(input())

    if action == 'spend':
        following_days += 1
        saved_money -= money
        if saved_money < 0:
            saved_money = 0

    elif action == 'save':
        saved_money += money
        following_days = 0

    if saved_money >= money_needed:
        print(f'You saved the money for {days_counter} days.')
        break

if following_days >= 5:
    print("You can't save the money.")
    print(f"{days_counter}")











