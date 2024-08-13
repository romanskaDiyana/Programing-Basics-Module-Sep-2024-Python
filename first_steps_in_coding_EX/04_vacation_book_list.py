# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги.
# Понеже Жоро предпочита да играе с приятели навън, вашата задача е да му помогнете да изчисли колко
# часа на ден трябва да отделя, за да прочете необходимата литература. 212 / 20 / 2
from math import floor

number_of_pages_in_one_book = int(input())
pages_per_hour = int(input())
number_of_days_to_read_one_book = int(input())

pages_per_day = floor(number_of_pages_in_one_book / pages_per_hour)
hours_to_read_every_day = int(pages_per_day / number_of_days_to_read_one_book)

print(hours_to_read_every_day)