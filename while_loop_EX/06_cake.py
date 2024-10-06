# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата,
# които гостите са взели преди тя да свърши. Ще получите размерите на тортата
# (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата "STOP"
# или докато не свърши тортата, броят на парчетата, които гостите вземат от нея
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
#     • "{брой парчета} pieces are left." -  ако стигнете до STOP и не са свършили парчетата торта;
#     • "No more cake left! You need {брой недостигащи парчета} pieces more."

cake_width = int(input())
cake_length = int(input())

total_cake_pieces = cake_width * cake_length

while True:
    new_input = input()
    if new_input == 'STOP':
        print(f"{total_cake_pieces} pieces are left.")
        break

    total_cake_pieces -= int(new_input)

    if total_cake_pieces <= 0:
        print(f"No more cake left! You need {abs(total_cake_pieces)} pieces more.")
        break

