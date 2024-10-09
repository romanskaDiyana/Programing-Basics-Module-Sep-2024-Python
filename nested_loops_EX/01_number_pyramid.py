# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида:

n = int(input())

current_number = 1

for row in range(1, n + 1):
    for column in range(1, row + 1):
        if current_number > n:
            break
        print(current_number, end=" ")
        current_number += 1

    print()



