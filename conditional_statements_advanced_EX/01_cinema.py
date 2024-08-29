# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
#     • Premiere - премиерна прожекция, на цена 12.00 лева;
#     • Normal - стандартна прожекция, на цена 7.50 лева;
#     • Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в
# залата (цели числа), въведени от потребителя, и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.

projection_type = input()
rows = int(input())
columns = int(input())

ticket_price = 0
people_summary = rows * columns
total_summary_price = 0

if projection_type == 'Premiere':
    total_summary_price = people_summary * 12
elif projection_type == 'Normal':
    total_summary_price = people_summary * 7.50
elif projection_type == 'Discount':
    total_summary_price = people_summary * 5

print(f'{total_summary_price:.2f}')


