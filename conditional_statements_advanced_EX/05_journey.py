# Млад програмист разполага с определен бюджет и свободно време в даден сезон.
# Напишете програма, която да приема на входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и
# колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи.
# Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
#     • При 100 лв. или по-малко - някъде в България:
#         ◦ Лято - 30% от бюджета;
#         ◦ Зима - 70% от бюджета.
#     • При 1000 лв. или по малко - някъде на Балканите:
#         ◦ Лято - 40% от бюджета;
#         ◦ Зима - 80% от бюджета.
#     • При повече от 1000 лв. - някъде из Европа:
#         ◦ При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
#     • Бюджет - реално число;
#     • Един от двата възможни сезона - "summer” или "winter”.
# Изход
# На конзолата трябва да се отпечатат два реда:
#     •  "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
#     • "{Вид почивка} - {Похарчена сума}":
#         ◦ Почивката може да е между "Camp" и "Hotel"
#         ◦ Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая

budget = float(input())
season = input()

place_to_rest = ''
vacation_cost = 0
destination = ''

if budget <= 100:
    if season == 'summer':
        vacation_cost = budget * 0.30
        place_to_rest = 'Camp'
        destination = 'Bulgaria'
    elif season == 'winter':
        vacation_cost = budget * 0.70
        place_to_rest = 'Hotel'
        destination = 'Bulgaria'
elif budget > 100 and budget <= 1000:
    if season == 'summer':
        vacation_cost = budget * 0.40
        place_to_rest = 'Camp'
        destination = 'Balkans'
    elif season == 'winter':
        vacation_cost = budget * 0.80
        place_to_rest = 'Hotel'
        destination = 'Balkans'
elif budget > 1000:
    if season == 'summer':
        vacation_cost = budget * 0.90
        place_to_rest = 'Hotel'
        destination = 'Europe'
    elif season == 'winter':
        vacation_cost = budget * 0.90
        place_to_rest = 'Hotel'
        destination = 'Europe'

print(f"Somewhere in {destination}")
print(f"{place_to_rest} - {vacation_cost:.2f}")
