# Напишете програма, която до получаване на командата "Stop",
# чете цели числа, въведени от потребителя, намира най-малкото измежду тях и го принтира.
# Въвежда се по едно число на ред.

import sys

min_number = sys.maxsize
command = input()

while command != 'Stop':
    number = int(command)

    if number <= min_number:
        min_number = number

    command = input()

print(min_number)