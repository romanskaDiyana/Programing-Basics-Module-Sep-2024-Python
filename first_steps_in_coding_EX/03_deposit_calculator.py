# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент.
# Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_sum = float(input())
deposit_term = int(input())
increase_per_year = float(input())

total_summury = deposit_sum + deposit_term * ((deposit_sum * (increase_per_year/100) / 12))

print(total_summury)