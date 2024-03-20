#Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, 
#виводячи імена всіх піддиректорій та файлів. 
#Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

#Вимоги до завдання:
#Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
#Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
#Використання бібліотеки colorama для реалізації кольорового виведення.
#Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
#Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

from colorama import Fore
import sys
from pathlib import Path

def get_dir_content(path:Path, step:str = "    "):
        print(f"{step}∟ " + Fore.BLUE + f"{path.name}" + Fore.RESET)
        for obj in path.iterdir():
            if obj.is_dir():
                get_dir_content(obj, step + "|   ")
            else:
                print(f"{step}|   ∟ " + Fore.GREEN + f"{obj.name}" + Fore.RESET)



def main():
    if len(sys.argv)>=2:
        try:
            path = Path(sys.argv[1]) 
            path = Path.absolute(path)
            if path.exists(follow_symlinks=True):
                print(Fore.BLUE + f"{path}" + Fore.RESET)
                get_dir_content(path)
            else:
                print("No path found for display")
        except Exception:
            print("Something goes wrong")
    else:
        print("path not entered")



if __name__ == "__main__":
    main()
