# 2.2 Основы Python

# 4 Переменные
f = 100
print((f - 32) * 5 / 9)

# 5 Операции с данными
# Задание 1
grams = 12345
full_kilograms = grams // 1000
print(f"В {grams} граммах содержится {full_kilograms} килограмм")

# Задание 2
number = 1234
last_digit = number % 10
print(f"Последняя цифра числа {number}: {last_digit}")

# Задание 3
numbers = [-4, 0, 5, 10,]
for number in numbers:
    if (number % 2 == 0) and (number > 0):
        print(f"число {number} является положительным и четным")
    else:
        print(f"число {number} не подходит под условия")

# Задание 4
numbers = [-5, 50, 120]
for number in numbers:
    if 0 < number < 100:
        print(f"число {number} находится в пределах диапазона от 0 до 100")
    else:
        print(f"число {number} выходит за пределы диапазона от 0 до 100")

# Задание 5
numbers = [-6, 3, 6, 8]
for number in numbers:
    if number % 3 != 0:
        print(f"число {number} не кратно 3")
    else:
        print(f"число {number} кратно 3")


# 6 Коллекции данных
# Задание 1
numbers = [1, 2, 3]
numbers.append(5)
print(numbers)

# Задание 2
fruits = ['avokado', 'apple', 'orange']
fruits.remove('apple')
print(fruits)

# Задание 3
cities = ['Moscow', 'London', 'Tbilisi']
print(cities[1])

# Задание 4
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[3:7])

# Задание 5
colors = ['red', 'blue', 'green']
colors[1] = 'yellow'
print(colors)

# Задание 6
animals = ['cat', 'dog', 'rabbit', 'hamster']
print(len(animals))

# Задание 7
student = {'name': 'ivan', 'age': 20}
student['grade'] = 'A'
print(student)

# Задание 8
student = {'name': 'ivan', 'age': 20, 'grade': 'B'}
student['grade'] = 'C'
print(student)

# Задание 9
student = {'name': 'ivan', 'age': 20, 'grade': 'B'}
del student['age']
print(student)

# Задание 10
student = {'name': 'ivan', 'age': 20, 'grade': 'B'}
print(f"Имя студента: {student['name']}")

# Задание 11
student = {'name': 'ivan', 'age': 20, 'grade': 'B'}
if 'grade' in student:
    print(f"Ключ 'grade' найден в словаре")
else:
    print(f"Ключ 'grade' не найден в словаре")

# Задание 12
student = {'name': 'ivan', 'age': 20, 'grade': 'B', 'address': {'city': 'Moscow', 'street': "lenina"}}
student['address']['city'] = 'Saint Petersburg'
print(student['address']['city'])

# Задание 13
student = {'name': 'Maria', 'grades': [1, 2, 3]}
student['grades'][0] = 5
print(student)

# Задание 14
student = [{'name': 'Maria', 'age': 20}, {'name': 'Petya', 'age': 30}]
student[0]['age'] = 35
print(student)

# Задание 15
colors = ('red', 'green', 'blue')
f = 'green' in colors
l = len(colors)
print(f'Наличие green: {f}. Длина кортежа: {l}')