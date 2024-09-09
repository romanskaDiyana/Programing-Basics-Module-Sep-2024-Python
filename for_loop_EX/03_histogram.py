# Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент
# p1 са под 200, друг процент
# p2 са от 200 до 399,
# друг процент p3 са от 400 до 599,
# друг процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре.
# Да се напише програма, която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.

numbers_count = int(input())

p1_counter = p2_counter = p3_counter = p4_counter = p5_counter = 0

for i in range(0, numbers_count):
    number = int(input())

    if number < 200:
        p1_counter += 1
    elif 200 <= number <= 399:
        p2_counter += 1
    elif 400 <= number <= 599:
        p3_counter += 1
    elif 600 <= number <= 799:
        p4_counter += 1
    elif number >= 800:
        p5_counter += 1

print(f'{p1_counter / numbers_count * 100:.2f}%')
print(f'{p2_counter / numbers_count * 100:.2f}%')
print(f'{p3_counter / numbers_count * 100:.2f}%')
print(f'{p4_counter / numbers_count * 100:.2f}%')
print(f'{p5_counter / numbers_count * 100:.2f}%')
