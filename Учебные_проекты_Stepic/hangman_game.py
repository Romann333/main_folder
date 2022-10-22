import random
word_list = ["автобус", "сосиска", "гантеля", "яблоко", "барабан", "вилка", "холодильник", "сковорода"]
b = 'д'          # Ответ на вопрос будете или игра, первый запуск сразу ДА)
guessed_words = []                 # список уже названных слов

def get_word():

    global word
    word = random.choice(word_list)
    word =  word.upper()

# функция получения текущего состояния

def display_hangman(tries):

    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                ''']
    return stages[tries]

def play(word):

    global b   
    guessed_letters = []               # список уже названных букв
    tries = 6                          # количество попыток
    word_completion = '_' * len(word)

    print()
    print('Давайте играть в угадайку слов!')
    print()
    print('У Вас есть 6 попыток, чтобы угадать слово. Вводите по одной букве или слово целиком.')
    print()
    print(display_hangman(tries))
    print()
    print('_' * len(word), 'Слово состоит из', len(word), 'букв.', 'Первая буква ', word[0], 'последняя ', word[-1])
    print()
    
    while True:
        
        
        a = input('Введите букву или слово целиком:  ').upper()
        
        if tries == 0:

            print(display_hangman(tries))
            print('Игра окончена вы проиграли... ')
            print(f'Загаданное слово было - {word}')
            b = input('Хотите сыграть еще разок?(д = да, н = нет): ')
            break
        
        if not a.isalpha():

            print()
            print('Нужно вводить ТОЛЬКО БУКВЫ,внимательней!!!')
            print()
            print(word_completion)
            print()
            continue
                    
        if a == word:

            print()
            print('Поздравляю вы угадали слово, игра окончена!')
            guessed_words.append(word)
            print(f'Загаданное слово было - {word}')
            b = input('Хотите сыграть еще разок?(д = да, н = нет):  ')
            break

        if a in guessed_letters:                 # угадана ли уже буква ранее
            print('Эту букву Вы уже отгадали, введите другую: ')
            print()
            print(word_completion)
            print()
            continue

        if a in word:                     #есть ли буква в  загаданном  слове
            guessed_letters.extend(a)     # добравляем букву в список
        else:
            tries -= 1
            print(display_hangman(tries))
            print()
            print(f'Упс.. Вы ошиблись! Осталось {tries} попыток.')
            print()
            print(word_completion)
            print()
            continue
        
        word_completion = ''
   
        for i in word:

            if i in guessed_letters:
                word_completion += i
            else:
                word_completion += '_'

        print()
        print(word_completion)
        print()

        if word_completion == word:

            print('Вы угадали слово, поздравляем!!! Игра окончена!')
            print()
            guessed_words.append(word)
            b = input('Хотите сыграть еще разок?(д = да, н = нет):  ')
            break

while True:
    
    if len(guessed_words) == len(word_list):
        print('База слов закончилась. Спасибо за игру. До свидания!')
        break

    if b == 'д':
        get_word()
        if word in guessed_words:
            continue
        else:
            play(word)

    else:
        print()
        print('Спасибо за игру. Приходите еще. Пока.. ')
        break


