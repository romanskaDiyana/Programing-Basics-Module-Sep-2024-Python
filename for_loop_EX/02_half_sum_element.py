# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и проверява дали
# сред тях съществува число, което е равно на сумата на всички останали.
#     • Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
#     • Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия
#     елемент и сумата на останалите (по абсолютна стойност)

import sys

count_of_numbers = int(input())

max_number = - sys.maxsize
sum_numbers = 0

for n in range(0, count_of_numbers):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    sum_numbers += current_number

if sum_numbers - max_number == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    sum_numbers = sum_numbers - max_number
    print(f'No\nDiff = {abs(max_number - sum_numbers)}')




        

