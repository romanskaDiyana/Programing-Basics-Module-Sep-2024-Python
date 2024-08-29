# Атанас решава да прекара отпуската си в Банско и да кара ски. Преди да отиде обаче,
# трябва да резервира хотел и да изчисли колко ще му струва престоя. Налични са следните видове помещения,
# със следните цени за престой:
#             ▪ "room for one person" – 18.00 лв за нощувка
#             ▪ "apartment" – 25.00 лв за нощувка
#             ▪ "president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението,
# което ще избере, той може да ползва различно намаление.
# Намаленията са както следва:
# След престоя, оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.
# Вход
# Входът се чете от конзолата и се състои от три реда:
#     • Първи ред - дни за престой - цяло число в интервала [0...365]
#     • Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
#     • Трети ред - оценка - "positive"  или "negative"
# Изход
# На конзолата трябва да се отпечата един ред:
#     • Цената за престоят му в хотела, форматирана до втория знак след десетичната запетая.


days_for_resting = int(input())
room = input()
grade = input()

price = 0
total_price = 0
days_for_resting = days_for_resting - 1

if room == 'room for one person':
    price = days_for_resting * 18
elif room == 'apartment':
    if days_for_resting <= 11:
        price = days_for_resting * 25 - ((days_for_resting * 25) * 0.30)
    elif days_for_resting > 11 and days_for_resting <= 15:
        price = days_for_resting * 25 - ((days_for_resting * 25) * 0.35)
    elif days_for_resting > 15:
        price = days_for_resting * 25 - ((days_for_resting * 25) * 0.50)
elif room == 'president apartment':
    if days_for_resting <= 11:
        price = days_for_resting * 35 - ((days_for_resting * 35) * 0.10)
    elif days_for_resting > 11 and days_for_resting <= 15:
        price = days_for_resting * 35 - ((days_for_resting * 35) * 0.15)
    elif days_for_resting > 15:
        price = days_for_resting * 35 - ((days_for_resting * 35) * 0.20)

if grade == 'positive':
    total_price = price + (price * 0.25)
else:
    total_price = price - (price * 0.10)

print(f"{total_price:.2f}")
