# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
#     • Пъзел - 2.60 лв.
#     • Говореща кукла - 3 лв.
#     • Плюшено мече - 4.10 лв.
#     • Миньон - 8.20 лв.
#     • Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде  на екскурзия.

trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

total_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count
total_price = puzzles_price * puzzles_count \
              + dolls_price * dolls_count \
              + bears_price * bears_count \
              + minions_price * minions_count \
              + trucks_price * trucks_count

if total_count >= 50:
    total_price -= total_price * 0.25

rent = total_price * 0.10

amount = total_price - rent

if amount >= trip_price:
    print(f"Yes! {(amount - trip_price):.2f} lv left.")
else:
    print(f"Not enough money! {(trip_price-amount):.2f} lv needed.")