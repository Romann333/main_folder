# Реализуйте функцию filter_string(). Она принимает на вход строку и символ и возвращает новую строку,
# в которой удалён переданный символ во всех его позициях. На этот раз реализуйте эту функцию с помощью цикла for. 
# Дополнительное условие: регистр исключаемого символа не имеет значения.

# Итоговая строка также не должна содержать концевые пробелы:

def filter_string(text,delete_char):

    result = ""

    for current_char in text:

        if current_char. lower() != delete_char.lower():
            result += current_char

    return result.strip()


text = 'If I look forward I win'

print(filter_string(text, 'i'))

print(filter_string(text, 'O'))
