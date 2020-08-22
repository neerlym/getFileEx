# -----------------------------------------------------------------------------
# Этот модуль содержит функцию get_file_list(), которая принимает путь до
# каталога, а возвращает список файлов в данном каталоге.
# Каждый элемент списка представляет собой список из 3-х элементов: имени
# файла, даты и времени модификации, и размера.
# Если файлов в данном каталоге нет, возвращается пустой список.
# Сигнатура : get_file_list(path) -> []
# -----------------------------------------------------------------------------

import os
import datetime


def get_file_list(path):
    if path[-1] != '/':
        # Модифицируем путь так, чтобы в конце он содержал косую черту.
        # Это нужно для простого добавления к пути имени файла/каталога.
        path = path + "/"
    # Получаем список всех файлов и каталогов в заданном каталоге.
    all_list = os.listdir(path=path)
    # Формируем новый список и оставляем там только список файлов.
    # (каталоги не включаем)
    file_list = []
    for item in all_list:
        file_path = path + item
        if not os.path.isdir(file_path):
            modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            ).strftime("%Y-%m-%d %H:%M:%S")
            size = str(os.path.getsize(file_path))
            file_list.append([item, modified_date, size])
    return file_list


if __name__ == "__main__":
    print("*** module get_file_list.py ***")
    my_list = get_file_list("./")
    print(my_list)
