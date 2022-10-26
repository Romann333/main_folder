import urllib.parse


url = 'https://docs-python.ru/standart-library/modul-urllib-parse-python/funktsija-unquote-unquote-plus-modulja-urllib-parse/'

url = urllib.parse.quote_plus(url)

url = urllib.parse.unquote_plus(url)

print(url)