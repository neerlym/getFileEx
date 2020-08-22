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

import sys


def get_params():
    # Функция возвращает полученные параметры из командной строки.
    # Позже можно переписать с использованием библиотеки argparse.
    arg_count = len(sys.argv)
    if arg_count < 2 or arg_count > 3:
        # Ожидается один или два параметра.
        # Позже переписать с использованием исключений!
        print("Неверное количество аргументов!")
        exit(1)
    ex = sys.argv[1]
    if arg_count == 3:
        path = sys.argv[2]
    else:
        path = None
    # Параметры возвращаются в виде словаря.
    return {
        "extension": ex,
        "path": path
    }


if __name__ == "__main__":
    params = get_params()
    print("path = " + str(params.get("path")))
    print("extension = " + str(params.get("extension")))
