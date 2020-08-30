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
import argparse

from modules.get_file_ex import get_file_ex
from modules.get_file_info import get_mdate
from modules.get_file_info import get_size


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('extension', nargs='?', default="*")
    parser.add_argument('path', nargs='?', default=os.getcwd())
    return parser


def to_fixlen(str, max_len = 40):
    i_len = len(str)
    if i_len < max_len:
        str = str + ' ' * (max_len - i_len)
    return str


if __name__ == "__main__":
    parser = create_parser()
    params = parser.parse_args(sys.argv[1:])

    ext = params.extension
    if ext != "" and ext[0] == '.':
        ext = ext[1:]
    path = params.path

    print(f"path = {path}\nextension = .{ext}\n")

    ex_list = get_file_ex(path, ext)

    print(f"count of elements: {len(ex_list)}\n")

    max_len = max(map(len, ex_list)) + 1
    for filename in ex_list:
        file_path = f"{path}\\{filename}"
        print(to_fixlen(filename, max_len=max_len), end=' ')
        print(get_mdate(file_path), end=' ')
        print(get_size(file_path))
