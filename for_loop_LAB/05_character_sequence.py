# Напишете програма, която чете текст (стринг), въведен от потребителя и печата всеки символ от текста на отделен ред.

sequence = input()

for char in range(len(sequence)):
    print(sequence[char])