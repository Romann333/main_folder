#Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины. 
#принимает на вход два аргумента (строку и длину) 
#и возвращает подстроку, начиная с первого символа:


def my_substr(string, lenth_of_string):

    index = 0
    sub_string = ''

    while index <= lenth_of_string - 1:

        current_char = string[index]
        sub_string += current_char
        index += 1

    return sub_string


string = 'If I look back I am lost'

print(my_substr(string, 1))
print(my_substr(string, 7))