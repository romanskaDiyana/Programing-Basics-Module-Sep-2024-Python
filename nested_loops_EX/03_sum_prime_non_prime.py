# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
# ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
# В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
#     • "Sum of all prime numbers is: {prime numbers sum}"
#     • "Sum of all non prime numbers is: {nonprime numbers sum}"
# Просто цяло число се дели на себе си и на 1, има поне 2 положителни делителя. Сложно се дели
# на себе си, на 1 и на други цели числа.

sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    non_prime_number = False
    new_input = input()

    if new_input == "stop":
        break

    new_number = int(new_input)

    if new_number < 0:
        print("Number is negative.")
        continue

    if new_number <= 1:
        sum_non_prime_numbers += new_number
        non_prime_number = True

    else:
        for number in range(2, int(new_number ** 0.5) + 1):
            if new_number % number == 0:
                sum_non_prime_numbers += new_number
                non_prime_number = True
                break

    if not non_prime_number:
        sum_prime_numbers += new_number

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")