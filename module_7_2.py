def custom_write(file_name, strings):
    """
    Записывает строки в файл и возвращает словарь с их позициями.

    :param file_name: Название файла для записи.
    :param strings: Список строк для записи.
    :return: Словарь, где ключ - кортеж (<номер строки>, <байт начала>), значение - строка.
    """
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            position = file.tell()  # Текущая позиция указателя в байтах
            strings_positions[(line_number, position)] = string
            file.write(string + '\n')  # Записываем строку с переходом на новую строку

    return strings_positions


# Тестирование программы
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)
