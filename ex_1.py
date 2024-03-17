#Вимоги до завдання:
#Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
#Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
#Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

def total_salary(path:Path)->tuple:
  sum = 0
  peoples = 0
  try:
    with open(path, "r", encoding="utf-8") as file
    lines = file.readlines()
    for line in lines:
      _, salary = line.split(",")
      peoples += 1
      sum += real(salary)
    return sum , sum/peoples
  except Exception:
    print("Error")
    return None
  
