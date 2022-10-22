print('Программа по шифрованию и дешифрованию сообщений по методу Цезаря')
print()
a = input('Вы хотите зашифровать сообщение или расшифровать? (ш = шифровать, д = дешифровать)')
b = input('Какой язык сообщения вы будете использовать? (рус = русский, анг = английский)')
c = input('Введите текст сообщения .. ')
v1 = ord('а')
v2 = ord('А')
v3 = ord('a')
v4 = ord('A')
if a == 'ш':
    if b == 'рус':
        d = int(input('Введите сдвиг шифрования от 1 до 31... '))
        for i in c:
            if i.islower() and i.isalpha():
                i = chr(v1 + ((ord(i) - v1) + d) % 32)
            if i.isupper() and i.isalpha():
                i = chr(v2 + ((ord(i) - v2) + d) % 32)
            print(i, end='')

    elif b == 'анг':
        d = int(input('Введите сдвиг шифрования от 1 до 25... '))
        for i in c:
            if i.islower() and i.isalpha():
                i = chr(v3 + ((ord(i) - v3) + d) % 26)
            if i.isupper() and i.isalpha():
                i = chr(v4 + ((ord(i) - v4) + d) % 26)
            print(i, end='')



elif a == 'д':        
    if b == 'рус':
        d = int(input('Введите сдвиг шифрования от 1 до 31... '))
        for i in c:
            if i.islower() and i.isalpha():
                i = chr(v1 + ((ord(i) - v1) - d) % 32)
            if i.isupper() and i.isalpha():
                i = chr(v2 + ((ord(i) - v2) - d) % 32)
            print(i, end='')

    elif b == 'анг':
        q = int(input('Введите сдвиг шифрования от 1 до 25... '))
        for d in range(q):
            for i in c:
                if i.islower() and i.isalpha():
                    i = chr(v3 + ((ord(i) - v3) - d) % 26)
                if i.isupper() and i.isalpha():
                    i = chr(v4 + ((ord(i) - v4) - d) % 26)
                print(i, end='')
            print()    
print()
