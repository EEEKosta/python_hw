# Задача 1: Вычисление площади прямоугольника
def rectangle_area(a, b):
    area = a * b
    print(area)

rectangle_area(5, 3)

# Задача 2: Перевод времени из секунд в часы и минуты
def convert_seconds(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    return (hours, minutes)

seconds = 3672
h, m = convert_seconds(seconds)

print(f'В {seconds} секундах содержится {h} час(ов) и {m} минут(ы).')

# Задача 3: Функция с аргументом по умолчанию
def power_of(number, exponent=2):
    result = number ** exponent
    return result

num1, exp1 = 3, 4
res1 = power_of(num1, exp1)
print(f'Число {num1} в степени {exp1} равно {res1}')

num2 = 5
res2 = power_of(num2)
print(f'Число {num2} в степени 2 равно {res2}')

# Задача 4: Подсчёт элементов
def count_items(*args):
    return len(args)

res1 = count_items(1, 2, 3, 4, 5)
print(f'Количество переданных элементов: {res1}')

res2 = count_items('apple', 'banana', 'cherry')
print(f'Количество переданных элементов: {res2}')
