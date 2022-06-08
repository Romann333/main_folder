# Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:


def join_numbers_from_range(first_num, last_num):

    result = ''
    index = first_num

    while index <= last_num:
        result += str (index)
        index += 1

    return result

print(join_numbers_from_range(3,8))