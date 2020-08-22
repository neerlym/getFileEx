# -----------------------------------------------------------------------------
# Модуль содержит функцию get_file_ex(), которая возвращает список
# всех файлов в указанном каталоге с указанным расширением.
# Если в каталоге нет файлов, функция возвращает пустой список.
# Если расширение указано как пустая строка "", функция возвращает список
# файлов без расширения (если такие имеются, иначе возвращает пустой список).
# Сигнатура : get_file_ex(path, extension) -> [ ... ]
# -----------------------------------------------------------------------------

from modules.get_extension import get_ex
from modules.get_file_list import get_file_list


def get_file_ex(path, ex):
    file_list = get_file_list(path)
    if ex == "*":
        return file_list
    ex_list = list(filter(lambda item: get_ex(item) == ex, file_list))
    return ex_list


if __name__ == "__main__":
    print("*** module get_file_ex.py ***")
    print(get_file_ex("./", "py"))
