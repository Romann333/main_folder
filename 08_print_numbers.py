# Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке. 

def print_numbers(max_number):

    while 0 < max_number:
        print (max_number)
        max_number -= 1

    print('finished!')  


print(print_numbers(8))