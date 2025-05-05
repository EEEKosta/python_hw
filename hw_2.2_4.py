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


