# Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений) и возвращает пару, 
# значения которой расположены строго в порядке возрастания.

def sort_pair(two_numbers):

    if (two_numbers)[0] >= (two_numbers)[1]:

        return (two_numbers)[1], (two_numbers)[0]

    return (two_numbers)[0], (two_numbers)[1]

print(sort_pair((5, 1)))

print(sort_pair((2, 2)))

print(sort_pair((7, 8)))