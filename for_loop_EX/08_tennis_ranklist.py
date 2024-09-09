# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки,
# които зависят от позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
#     • W - ако е победител получава 2000 точки
#     • F - ако е финалист получава 1200 точки
#     • SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири,
# като знаете с колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни
# турнири и колко процента от турнирите е спечелил.
import math

tournament_count = int(input())
starting_points = int(input())

total_points = 0
average_points = 0
counter_wins = 0
percent_wins = 0

for tournament in range(0, tournament_count):
    tournament_exit = input()

    if tournament_exit == 'W':
        total_points += 2000
        counter_wins += 1
    elif tournament_exit == 'F':
        total_points += 1200
    elif tournament_exit == 'SF':
        total_points += 720

average_points = total_points / tournament_count
total_points += starting_points
percent_wins = counter_wins / tournament_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_wins:.2f}%")