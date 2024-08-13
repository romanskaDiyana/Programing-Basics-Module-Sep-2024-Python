# Дадено е цяло число – начален брой точки. Върху него се начисляват бонус точки по правилата,
# описани по-долу. Да се напише програма, която пресмята бонус точките, които получава числото
# и общия брой точки (числото + бонуса).
#     • Ако числото е до 100 включително, бонус точките са 5;
#     • Ако числото е по-голямо от 100, бонус точките са 20% от числото;
#     • Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
#     • Допълнителни бонус точки (начисляват се отделно от предходните):
#         ◦ За четно число  + 1 т.
#         ◦ За число, което завършва на 5  + 2 т.

starting_points = int(input())
bonus_points = 0

if starting_points <= 100:
    bonus_points = 5
elif starting_points <= 1000:
    bonus_points = starting_points * 0.20
elif starting_points > 1000:
    bonus_points = starting_points * 0.10

if starting_points % 2 == 0:
    bonus_points += 1
if starting_points % 10 == 5:
    bonus_points += 2


print(f'{bonus_points}')
print(f'{bonus_points + starting_points}')