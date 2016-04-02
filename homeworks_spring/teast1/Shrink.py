import argparse
import os
from os import listdir
import subprocess

parser = argparse.ArgumentParser(description='Сжатие картинки по указанным процентам без регистрации и смс')
parser.add_argument("percent",
                    type=int,
                    help='Проценты')
parser.add_argument("path",
                    type=str,
                    help="Полный путь до файла")
parser.add_argument("path_new",
                    type=str,
                    nargs='?',
                    help="Новый путь для сохранения изменённного изображения")

args = parser.parse_args()
percent = args.percent
path = args.path
path_new = args.path_new
file_name = path.split('/')[-1]
percent = str(percent)+'%'


if os.path.isfile(path):
    if path_new == None:
        subprocess.call(' '.join(["convert", path, "-resize", percent, path]), shell=True)
    else:
        if os.path.isfile(path_new):
            subprocess.call(' '.join(["convert", path, "-resize", percent, path_new]), shell=True)
        elif os.path.isdir(path_new):
            subprocess.call(' '.join(["convert", path, "-resize", percent, path_new+file_name]), shell=True)
elif os.path.isdir(path):
    files = listdir(path)
    images = []
    images1 = filter(lambda x: x.endswith('.jpg'), files)
    images2 = filter(lambda x: x.endswith('.png'), files)

    for i in images1:
        images.append(i)
    for i in images2:
        images.append(i)

    if path_new == None:
        for i in images:
            subprocess.call(' '.join(["convert", path, "-resize", percent, path]), shell=True)
    else:
        if os.path.isfile(path_new):
            for i in images:
                subprocess.call(' '.join(["convert", path, "-resize", percent, path_new]), shell=True)
        elif os.path.isdir(path_new):
            for i in images:
                subprocess.call(' '.join(["convert", path, "-resize", percent, path_new+file_name]), shell=True)

