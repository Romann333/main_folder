import random
a = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определенно, ДА!", "Можешь быть уверен в этом", "Мне кажется - ДА", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - ДА", "Да", "Пока неясно попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", " Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? ')
print()
print(f'Привет, {name}!')
print()
question = input('Задай мне любой вопрос и ты получишь честный ответ! ')
while True:
    
    print(random.choice(a))
    print()
    question = input('Хочешь ли ты задать еще воросы? ')
    print()
    if question.lower() == 'да':
        q = input('Слушаю тебя..  ')
        print()
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
