# -----------------------------------------------------------------------------
# Этот модуль содержит функции, предоставляющие различную информацию о файле.
# Функция get_mdate(file_path) возвращает дату и время последней
# модификации файла в виде строки.
# Функция get_size(file_path) возвращает размер файла.
# -----------------------------------------------------------------------------

import os
import datetime


def get_mdate(file_path):
    mtime = os.path.getmtime(file_path)
    mdate = datetime.datetime.fromtimestamp(mtime)
    return mdate.strftime("%Y-%m-%d %H:%M:%S")


def get_size(file_path):
    size = os.path.getsize(file_path)
    postfix = ["B", "KB", "MB", "GB"]
    j = 0
    while size > 1024 and j <= len(postfix):
        size = size / 1024
        size = round(size, 2)
        j += 1
    return str(size) + postfix[j]


if __name__ == "__main__":
    print("*** module get_file_info.py ***")
    print(get_mdate("./get_file_info.py"))
    print(get_size("./get_file_info.py"))
