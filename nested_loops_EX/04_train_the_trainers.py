# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да
# помогнете на журито, което ще оценява презентациите, като напишете програма,
# в която да изчислява средната оценка от представянето на всяка една презентация от даден студент,
# а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

jury_number = int(input())
total_average_grade = 0
number_of_presentations = 0
score_per_presentation = 0
presentation_counter = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    presentation_counter += 1
    score_per_presentation = 0

    for score in range(jury_number):
        current_grade = float(input())
        score_per_presentation += current_grade

    score_per_presentation = score_per_presentation / jury_number
    print(f"{presentation_name} - {score_per_presentation:.2f}.")

    total_average_grade += score_per_presentation

print(f"Student's final assessment is {total_average_grade / presentation_counter:.2f}.")



