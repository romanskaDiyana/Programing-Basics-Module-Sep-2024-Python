# Ани отива до родния си град след много дълъг период извън страната.
# Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга.
# Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга или не провери всички книги в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст),
# която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
#     • Ако не открие търсената книгата да се отпечата на два реда:
#     • "The book you search is not here!"
#     • "You checked {брой} books."
#     • Ако открие книгата си се отпечатва един ред:
#         ◦ "You checked {брой} books and found it."

book_searching_for = input()
book_counter = 0
is_found = False

while True:
    current_book = input()

    if current_book == 'No More Books':
        break

    if current_book == book_searching_for:
        is_found = True
        print(f"You checked {book_counter} books and found it.")
        break

    book_counter += 1

if not is_found:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")


