#Ваше завдання - розробити функцію get_cats_info(path), 
#яка читає цей файл та повертає список словників з інформацією про кожного кота.

#Вимоги до завдання:
#Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
#Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

def get_cats_info(path:str)->list:
  result_list = []                                                #init list for result
  try:                                                            #try work with data
    with open(path, "r", encoding="utf-8") as file:               #open file for reading
      for line in file:                                           #read each row from file
        id, name, age = line.strip().split(",")                   #remove "\n" and split by ","
        result_list.append({"id":id, "name":name, "age": age})    #append to list new dictionary with required data
    return result_list                                            #return result
  except FileNotFoundError:                                       #if rise error regarding with file location
    print("File not found")                                       #print file not found
      