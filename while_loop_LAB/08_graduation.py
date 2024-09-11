# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
# а първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки.
# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
# като се отпечатва името на ученика и в кой клас бива изключен.
#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.

student_name = input()

year_counter = 0
counter_low_grade = 0
sum_of_grades = 0
average_grade = 0

while year_counter < 12:
    grade = float(input())

    if grade < 4:
        counter_low_grade += 1
        if counter_low_grade == 2:
            print(f"{student_name} has been excluded at {year_counter + 1} grade")
            break
        continue

    year_counter += 1
    sum_of_grades += grade

else:
    average_grade = sum_of_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
