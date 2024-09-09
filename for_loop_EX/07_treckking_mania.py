# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване.
# Според размера на групата, катерачите ще изкачват различни върхове.
#     • Група до 5 човека – изкачват Мусала
#     • Група от 6 до 12 човека – изкачват Монблан
#     • Група от 13 до 25 човека – изкачват Килиманджаро
#     • Група от 26 до 40 човека –  изкачват К2
#     • Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

groups_count = int(input())

counter_musala = counter_mont_blanc = counter_kilimangaro = counter_k2 = counter_everest = 0
total_count = 0

for group in range(0, groups_count):
    people_group_count = int(input())

    if people_group_count <= 5:
        counter_musala += people_group_count
    elif people_group_count >= 6 and people_group_count <= 12:
        counter_mont_blanc += people_group_count
    elif people_group_count >= 13 and people_group_count <= 25:
        counter_kilimangaro += people_group_count
    elif people_group_count >= 26 and people_group_count <= 40:
        counter_k2 += people_group_count
    elif people_group_count >= 41:
        counter_everest += people_group_count

    total_count += people_group_count

print(f'{(counter_musala / total_count * 100):.2f}%')
print(f'{(counter_mont_blanc / total_count * 100):.2f}%')
print(f'{(counter_kilimangaro / total_count * 100):.2f}%')
print(f'{(counter_k2 / total_count * 100):.2f}%')
print(f'{(counter_everest / total_count * 100):.2f}%')