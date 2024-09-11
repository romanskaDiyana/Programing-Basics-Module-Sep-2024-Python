# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
#     • при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
#     • при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

username = input()
correct_password = input()

password_attempt = input()
while password_attempt != correct_password:
    password_attempt = input()

print(f'Welcome {username}!')
