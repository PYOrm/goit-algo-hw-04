#Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

#Вимоги до завдання:
#Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
#Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

def get_cats_info(path:Path)->list:
  resalt_list =[]
  try:
    with open(path, "r", encoding="utf-8") as file
    while line = file.readline():
      id, name, age = line.split()
      result_list.append({"id":id, "name":name, "age": int(age)})
    return result_list
  except Exception:
    print("Error")
      
