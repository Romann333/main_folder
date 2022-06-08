#Реализуйте функцию is_palindrome(), которая принимает на вход слово, 
# определяет является ли оно палиндромом и возвращает логическое значение.


def is_palindrome(text):

    result = ""

    for char in text:
        result = char + result

    return result == text


print(is_palindrome(''))
print(is_palindrome('radar'))
print(is_palindrome('a'))
print(is_palindrome('abs'))
print(is_palindrome('ишак ищет у тещи каши'))