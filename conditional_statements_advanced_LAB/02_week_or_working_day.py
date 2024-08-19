# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

day_of_week = input()

if  day_of_week == 'Saturday' or 'Sunday':
    print('Weekend')
elif day_of_week == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
    print('Working day')
else:
    print('Error')