import argparse
import os.path
import shutil
import subprocess

parser = argparse.ArgumentParser(description='За полным описанием идеи обращаться к Косте (https://vk.com/askmebefore)',
                                 epilog="Иногда задания Кости очень странные")
parser.add_argument("command",
                    type=str,
                    choices=['store', 'diff'],
                    help='С позволения Константина разрешено только две команды: '
                         '"store" - сохранение текущего состояния файла и '
                         '"diff" - запуск стандартной утилиты diff')
parser.add_argument("path",
                    type=str,
                    help="Полный путь до файла, с путями до директорий не работаем")

args = parser.parse_args()
command = args.command
path = args.path

dir_for_save = 'D:/Users/Leo/Jupyter/sad'
file_name = path.split('/')[-1]
new_path = 'D:/Users/Leo/Jupyter/sad/' + file_name

if command == 'store':
    if os.path.isdir(path):
        print('Мы так не договаривались, я не знаю, что делать с папками!')
    else:
        shutil.copy(path, dir_for_save)
elif command == 'diff':
    subprocess.call(' '.join(['FC ', path, new_path]), shell=True)
