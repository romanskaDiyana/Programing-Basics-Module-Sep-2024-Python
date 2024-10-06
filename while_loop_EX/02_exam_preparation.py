# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка.
# Програмата трябва да приключи прочитането на данни при команда
# "Enough" или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход
#     • На първи ред - брой незадоволителни оценки - цяло число;
#     • След това многократно се четат по два реда:
#         ◦ Име на задача – текст;
#     • Оценка - цяло число в интервала [2…6


max_negative_grades = int(input())

average_grade = 0
total_grade = 0
number_of_tasks = 0
last_task_name = ''
counter_negative_grades = max_negative_grades

while counter_negative_grades > 0:

    input_name = input()

    if input_name == 'Enough':
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {number_of_tasks}")
        print(f"Last problem: {last_task_name}")
        break

    grade = int(input())

    if grade <= 4:
        counter_negative_grades -= 1

    if counter_negative_grades == 0:
        print(f"You need a break, {max_negative_grades} poor grades.")

    number_of_tasks += 1
    total_grade += grade
    average_grade = total_grade / number_of_tasks
    last_task_name = input_name




