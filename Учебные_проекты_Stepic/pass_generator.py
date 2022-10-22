import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
q1 = int(input('Сколько паролей необходимо сгенерировать?'))
q2 = int(input('Введите длинну одного пароля?'))
q3 = input('Включать ли цифры от 0 до 9?(д = да, н = нет)')
q4 = input('Включать ли большие буквы?(д = да, н = нет)')
q5 = input('Включать ли строчные быквы?(д = да, н = нет)')
q6 = input('Включать ли символы?(д = да, н = нет)')
q7 = input('Исключать ли неоднозначные символы: il1L0Oo?(д = да, н = нет)')

if q3 == 'д':
    chars += digits
if q4 == 'д':
    chars += uppercase_letters
if q5 == 'д':
    chars += lowercase_letters
if q6 == 'д':
    chars += punctuation
if q7 == 'д':
    s = '1ilLoO0'
    for i in s:
        chars = chars.replace(i, '')
for e in range(q1):
    password = ''
    for i in range(q2):
        password += random.choice(chars)
    print(password)
