# -----------------------------------------------------------------------------
# Модуль содержит функцию get_file_ex(), которая возвращает список
# всех файлов в указанном каталоге с указанным расширением.
# Если исходный список пуст, функция также возвращает пустой список.
# Если расширение указано как пустая строка "", функция возвращает список
# файлов без расширения (если такие имеются, иначе возвращает пустой список).
# Сигнатура : get_file_ex(file_list, extension) -> []
# -----------------------------------------------------------------------------

from get_extension import get_ex
from get_file_list import get_file_list


def get_file_ex(file_list, ex):
    ex_list = list(filter(lambda item: get_ex(item) == ex, file_list))
    return ex_list


if __name__ == "__main__":
    print("*** module get_file_ex.py ***")
    print(get_file_ex(get_file_list("./"), "py"))
