# -----------------------------------------------------------------------------
# Программа выводит список всех файлов, имеющих данное расширение, из
# указанного каталога. Принимает два необязательных аргумента: расширение и
# путь до каталога.
# Если расширение указано как пустая строка "", выводятся все файлы без
# расширения. Если расширение указано как символ "*", выводятся файлы с любым
# расширением. Расширение может быть указано как с точкой, так и без неё
# (например "jpg" и ".jpg" эквивалентны).
# Если путь до каталога не указан, используется текущий каталог
# (из которого запущена программа). Если указан путь до не существующего
# каталога, или это не каталог, выводится соответствующее сообщение и
# программа завершается.
# Первый аргумент (расширение) обязателен, второй аргумент (путь до каталога)
# можно не указывать (тогда программа будет работать в текущем каталоге).
# -----------------------------------------------------------------------------

import os
import sys
from modules.get_file_ex import get_file_ex
from modules.get_file_info import get_mdate
from modules.get_file_info import get_size


def get_params():
    # Функция возвращает полученные параметры из командной строки.
    arg_count = len(sys.argv)
    if arg_count < 2 or arg_count > 3:
        # Ожидается один или два параметра.
        print("Неверное количество аргументов!")
        exit(1)
    ex = sys.argv[1]
    if arg_count == 3:
        path = sys.argv[2]
    else:
        path = None
    return {
        "extension": ex,
        "path": path
    }


def ex_value(params):
    # Возвращает значение extension, извлечённое из параметров.
    ex = params.get("extension")
    if ex != "" and ex[0] == '.':
        ex = ex[1:]
    return ex


def path_value(params):
    # Возвращает значение path, извлечённое из параметров.
    path = params.get("path")
    if path == None:
        path = os.getcwd()
    return path


if __name__ == "__main__":
    params = get_params()
    ex = ex_value(params)
    path = path_value(params)

    print(f"path = {path}\nextension = .{ex}\n")

    ex_list = get_file_ex(path, ex)

    print(f"count of elements: {len(ex_list)}\n")

    for i in ex_list:
        file_path = f"{path}\\{i}"
        print(i, get_mdate(file_path), get_size(file_path))
