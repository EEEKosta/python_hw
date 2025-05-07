# Условные конструкции - задачи
# Задача 1: Оценка по шкале
def check_grade(score):
    if 90 <= score <= 100:
        return 'Отлично'
    elif 75 <= score <= 89:
        return 'Хорошо'
    elif 50 <= score <= 74:
        return 'Удовлетворительно'
    elif 0 <= score < 50:
        return 'Неудовлетворительно'
    else:
        return 'Некорректная оценка'

score = 85
result = check_grade(score)
print(f'Оценка за {score} баллов: {result}\n')

# Задача 2: Чётное или нечётное число
def is_even(number):
    return 'чётное' if number % 2 == 0 else 'нечётное'

num1 = 4
result1 = is_even(num1)
print(f'Число {num1} является {result1}')

num2 = 7
result2 = is_even(num2)
print(f'Число {num2} является {result2}\n')

# Задача 3: Максимальное из двух чисел
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = 10
num2 = 20
max = find_max(num1, num2)
print(f'Максимальное из чисел {num1} и {num2}: {max}\n')

# Задача 4: Проверка числа на положительность и чётность
def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return f'Число {number} положительное и чётное'
        else:
            return f'Число {number} положительное, но нечётное'
    else:
        return f'Число {number} отрицательное'

print(check_number(8))
print(check_number(5))
print(check_number(-5), '\n')

# Задача 5: Проверка длины строки
def check_string_length(string, length):
    if len(string) > length:
        return 'Длина строки достаточная'
    else:
        return 'Строка слишком короткая'

# Примеры использования
str1 = 'Python'
str2 = 'Hi'
limit = 5

def check_string_length(string, length):
    if len(string) > length:
        print(f'Длина строки {string} достаточная')
    else:
        print(f'Строка {string} слишком короткая')

result1 = check_string_length(str1, limit)
result2 = check_string_length(str2, limit)
