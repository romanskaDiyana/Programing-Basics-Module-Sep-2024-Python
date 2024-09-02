# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

from math import fabs

numbers_count = int(input())

left_sum = 0
right_sum = 0

for _ in range (numbers_count):
    left_numbers = int(input())
    left_sum += left_numbers

for _ in range(numbers_count):
    right_numbers = int(input())
    right_sum += right_numbers

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')