# Да се напише програма, която чете текст (стринг), въведен от потребителя,
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:

word = input()

sum_letters = 0

for letter in range(len(word)):
    if word[letter] == 'a':
        sum_letters += 1
    elif word[letter] == 'e':
        sum_letters += 2
    elif word[letter] == 'i':
        sum_letters += 3
    elif word[letter] == 'o':
        sum_letters += 4
    elif word[letter] == 'u':
        sum_letters += 5
print(sum_letters)
