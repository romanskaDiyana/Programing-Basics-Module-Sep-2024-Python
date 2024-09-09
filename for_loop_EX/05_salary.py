# Шеф на компания забелязва че все повече служители прекарват  време в сайтове, които ги разсейват.
# За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си.
# Според отворения сайт в таба се налагат следните глоби:
#     • "Facebook" -> 150 лв.
#     • "Instagram" -> 100 лв.
#     • "Reddit" -> 50 лв.
tabs_number = int(input())
salary = int(input())
flag = False

for i in range (0, tabs_number):
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        flag = True
        break

if not flag:
    print(f'{abs(salary)}')

