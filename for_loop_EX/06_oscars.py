# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса.
# Академията ще ви даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка.
# Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките,
# които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата,
# че дадения актьор е получил номинация.

actor_name = input()
points_from_academy = float(input())
judges_count = int(input())

total_points = points_from_academy
is_nominated = False

for judge in range(0, judges_count):
    judge_name = input()
    points_given = float(input())

    total_points += ((len(judge_name) * points_given) / 2)

    if total_points > 1250.50:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {(total_points):.1f}!')
        is_nominated = True
        break

if not is_nominated:
    print(f"Sorry, {actor_name} you need {1250.50 - total_points:.1f} more!")

