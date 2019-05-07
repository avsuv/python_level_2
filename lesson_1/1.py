# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'

print(word_1, ' - ', type(word_1))
print(word_2, ' - ', type(word_2))
print(word_3, ' - ', type(word_3))
print()
word_1_converted = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_2_converted = '\u0441\u043e\u043a\u0435\u0442'
word_3_converted = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(word_1_converted, ' - ', type(word_1_converted))
print(word_2_converted, ' - ', type(word_2_converted))
print(word_3_converted, ' - ', type(word_3_converted))
