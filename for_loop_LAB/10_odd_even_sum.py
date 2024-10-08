# Да се напише програма, която чете n на брой цели числа, подадени от потребителя и проверява дали
# сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
#     • Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
#     • Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

from math import fabs

numbers_count = int(input())

even_sum = 0
odd_sum = 0
for index in range(numbers_count):
    number = int(input())
    if index % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')
