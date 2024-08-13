# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява
# дали се е справил със задачата, като се има предвид, че:
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави,
# в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
from math import floor

current_record = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

ivan_record_time = distance_in_meters * time_in_seconds_for_one_meter
water_resistance_seconds = floor(distance_in_meters / 15) * 12.5

ivan_final_record_time = ivan_record_time + water_resistance_seconds

if ivan_final_record_time >= current_record:
    print(f"No, he failed! He was {(ivan_final_record_time - current_record):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {(ivan_final_record_time):.2f} seconds.")




