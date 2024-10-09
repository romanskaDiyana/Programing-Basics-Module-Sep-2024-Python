# Вашата задача е да напишете програма, която да изчислява процента на билетите
# за всеки тип от продадените билети: студентски(student), стандартен(standard) и детски(kid),
# за всички прожекции. Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
#     • На първия ред до получаване на командата "Finish" - име на филма – текст
#     • На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
#     • За всеки филм, се чете по един ред до изчерпване на свободните места в
#     залата или до получаване на командата "End":
#         ◦ Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
#     • След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
#     • При получаване на командата "Finish" да се отпечатат четири реда:
#         ◦ "Total tickets: {общият брой закупени билети за всички филми}"
#         ◦ "{процент на студентските билети}% student tickets."
#         ◦ "{процент на стандартните билети}% standard tickets."
#         ◦ "{процент на детските билети}% kids tickets."

student_counter = 0
standart_counter = 0
kid_counter = 0
ticket_type = ""
student_percentage = 0
standart_percentage = 0
kid_percentage = 0
total_seats_taken = 0
percentage_of_full_room = 0
taken_seats_per_movie = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        print(f"Total tickets: {total_seats_taken}")
        print(f"{((student_counter * 100 ) / total_seats_taken):.2f}% student tickets.")
        print(f"{((standart_counter * 100)/ total_seats_taken):.2f}% standard tickets.")
        print(f"{((kid_counter * 100)/ total_seats_taken):.2f}% kids tickets.")
        break

    free_seats = int(input())
    current_seats = free_seats
    taken_seats_per_movie = 0

    while current_seats > 0:
        ticket_type = input()
        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standart_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1

        taken_seats_per_movie += 1
        current_seats -= 1

    total_seats_taken = student_counter + standart_counter + kid_counter
    percentage_of_full_room = (taken_seats_per_movie * 100) / free_seats

    print(f"{movie_name} - {percentage_of_full_room:.2f}% full.")

