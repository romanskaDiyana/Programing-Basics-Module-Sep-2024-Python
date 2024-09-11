# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред
import sys

max_number = -sys.maxsize
command = input()

while command != 'Stop':
    number = int(command)

    if number >= max_number:
        max_number = number

    command = input()

print(max_number)