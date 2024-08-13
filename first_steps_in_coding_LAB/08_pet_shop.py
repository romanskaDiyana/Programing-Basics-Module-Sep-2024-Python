# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.
# Храната се пазарува от зоомагазин, като една опаковка храна за кучета е на цена 2.50 лв,
# а опаковка храна за котки струва 4 лв.

dog_food_packages = int(input())
cat_food_number_of_packages = int(input())

dog_food_price = 2.50
cat_food_price = 4

total_sum = dog_food_packages*dog_food_price + cat_food_number_of_packages * cat_food_price

print(f'{total_sum} lv.')