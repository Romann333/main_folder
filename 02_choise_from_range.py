# Реализуйте функцию choice_from_range(), которая принимает строку-набор 
# и выбирает случайный символ по индексу из ограниченного диапазона.

import random

def choice_from_range(text, first_num, last_num):

    char = random.choice(text[first_num:last_num + 1])

    return char

text = "abcdef"

print(choice_from_range(text, 3, 5))

print(choice_from_range(text, 3, 5))

print(choice_from_range(text, 3, 5))