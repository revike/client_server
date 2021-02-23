"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

words = ['сетевое программирование', 'сокет', 'декоратор']
file = 'test_file.txt'

with open(file, 'w') as f:
    for word in words:
        f.write(word + '\n')

file_coding = locale.getpreferredencoding()
print(f'Кодировка -> {file_coding}\n')  # кодировка файла по умолчанию

with open(file, encoding=file_coding) as f:
    for result in f:
        print(result)
