# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
#     • От първия ред на входа се въвежда броят числа n.
#     • От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

numbers_count = int(input())

sum_numbers = 0
for n in range(numbers_count):
    number = int(input())
    sum_numbers += number

print(sum_numbers)