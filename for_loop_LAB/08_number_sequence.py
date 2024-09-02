# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.

from sys import maxsize

numbers_count = int(input())

max_number = -maxsize
min_number = maxsize

for i in range(numbers_count):
    number= int(input())
    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

