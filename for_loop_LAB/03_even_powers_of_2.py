# Да се напише програма, която чете число n, въведено от потребителя,
# и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.

number = int(input())

for n in range(number + 1):
    if n % 2 == 0:
        print(2 ** n)