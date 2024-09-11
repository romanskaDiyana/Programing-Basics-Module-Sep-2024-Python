# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа,
# докато тяхната сума стане по-голяма или равна на първоначалното число.
# След приключване на четенето да се отпечата сумата на въведените числа.

CONSTANT_NUMBER = int(input())

sum_of_numbers = 0

while sum_of_numbers < CONSTANT_NUMBER:
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)