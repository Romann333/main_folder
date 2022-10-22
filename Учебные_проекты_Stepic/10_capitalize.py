# Реализуйте функцию capitalize(), 
# которая принимает непустую строку и приводит первую букву строки к верхнему регистру:

def capitalize (str):
    return str[0]. upper() + str[1:]

print(capitalize('hexlet'))