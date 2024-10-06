# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с
# колко най-малко монети може да стане това.

change = float(input())
counter_coins = 0


while change > 0:
    if change >= 2:
        counter_coins += 1
        change -= 2
    elif 1 <= change < 2:
        counter_coins += 1
        change -= 1
    elif 0.50 <= change < 1:
        counter_coins += 1
        change -= 0.50
    elif 0.20 <= change < 0.50:
        counter_coins += 1
        change -= 0.20
    elif 0.10 <= change < 0.20:
        counter_coins += 1
        change -= 0.10
    elif 0.05 <= change < 0.10:
        counter_coins += 1
        change -= 0.05
    elif 0.02 <= change < 0.05:
        counter_coins += 1
        change -= 0.02
    elif change < 0.02:
        counter_coins += 1
        change -= 0.01

    change = round(change, 2)


print(f'{counter_coins}')