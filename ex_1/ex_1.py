#Вимоги до завдання:
#Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
#Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
#Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


def total_salary(path:str)->tuple:
  sum = 0                                             #init sum variable
  employees = 0                                       #init counter of employees
  try:                                                #try work with file and data
    with open(path, "r", encoding="utf-8") as file:   #open file for reading
      lines = file.readlines()                        #read all rows in list
      for line in lines:                              #take each row
        _, salary = line.split(",")                   #and split by ","
        employees += 1                                #increase employees counter
        sum += float(salary)                          #add employee salary to total
    return sum , sum/employees                        #if all OK return tuple (total_salary, average_salary)
  except FileNotFoundError:                           #if wrong path or file not found
    print(f"File not found")
  except ValueError:                                  #if data in file not correct
    print(f"Error data type")
  