# Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои от тях,
# като по този начин създаде уютна обстановка и комфорт на гостите си. За целта е наела фирма.
# Напишете програма, която изчислява необходимате сума, които Божидара ще трябва да заплати
# на фирмата изпълнител на проекта. Цената на един кв. м. е 7.61 лв със ДДС.
# Понеже нейният двор е доста голям, фирмата изпълнител предлага 18% отстъпка от крайната цена.

meters_to_be_green = float(input())

meters_price = 7.61

total_price = meters_to_be_green * meters_price
discount = total_price * 18/100
price_after_discount = total_price - discount


print(f'The final price is: {price_after_discount} lv.')
print(f'The discount is: {discount} lv.')