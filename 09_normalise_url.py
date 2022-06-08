# Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. 
# Она принимает адрес сайта и возвращает его с https:// в начале.
# Функция принимает адреса в виде:
# АДРЕС
# http://АДРЕС
# https://АДРЕС (уже нормализованный)
# и всегда возвращает адрес в виде https://АДРЕС.

def normalize_url(address):

    if address[:8] == "https://":
        return address
    elif address[:7] == "http://":
        return "https://" + address[7:]

    return "https://" + address


print(normalize_url('https://ya.ru'))

print(normalize_url('google.com'))

print(normalize_url('http://ai.fi'))