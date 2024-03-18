# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, 
#знаходити номер телефону за ім'ям, змінювати записаний номер телефону, 
#виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, 
#скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.

# Вимоги до завдання:
# Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
# Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. 
# Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. 
# В разі введення команди "exit" або "close", програма повинна завершувати виконання.
# Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
# Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
# Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.

import re

phone_book = {}

def check_phone_format(phone:str) -> bool:
    mask = "^[\+]?\d*"
    return bool(re.search(mask,phone).group())

def add_contact(data:dict) -> str:
        name, *_ = data
        if phone_book.get(name):
            confirm = input("Contact exist. Update contact? ").lower()
            if confirm not in ["y", "yes"]:
                return "Contact exist. Phone number not updated."
        phone_book.update(data)
        return "Record added."
        
def change_contact(data:dict) -> str:
    name, *_ = data
    if phone_book.get(name): 
        phone_book.update(data)
        return "Contact updated"
    return "Can't update. Record not found"  

def show_phone(data:dict) ->str:
    name, *_ = data
    return phone_book.get(name) if phone_book.get(name) else "Record not found"

def show_all() -> str:
    records = ""
    for name, phone in phone_book.items():
        records += f"{name:<30}{phone:>15}\n"
    return records
  
def parse_input(user_input:str) -> dict:
    user_input = user_input.lower().strip().split()
    command = ""
    number = ""
    name = ""
    if len(user_input):
        command = user_input.pop(0)
    if len(user_input):
        number = user_input.pop()
        for el in user_input:
            name = name + f"{el.capitalize()} " 
        if check_phone_format(number):
            name = name.strip() 
        else:
            name = name + number.capitalize() 
            number = ""   
    return {"command": command, "data":{name: number}}
      
def main():
    print("Welcome to the assistant bot!")
    while True:
        get_command = parse_input(input("Enter a command: "))
        match get_command.get("command"):
            case ("exit"|"close"):
                print("Good bye!")
                break
            case ("hello"):
                print("How can I help you?")
            case ("add"):
                print(add_contact(get_command.get("data")))
            case ("change"):
                print(change_contact(get_command.get("data")))
            case ("phone"):
                print(show_phone(get_command.get("data")))
            case ("all"):
                print(show_all())
            case (_):
                print("Invalid command.")

if __name__ == "__main__":
    main()