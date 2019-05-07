# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standart']
words_bytes = []
for word in words:
    words_bytes.append(word.encode('utf-8'))
    print(word.encode('utf-8'))
print()
for word in words_bytes:
    print(word.decode('utf-8'))

