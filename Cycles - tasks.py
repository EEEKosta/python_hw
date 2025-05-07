# Циклы - задачи
# Задача 1: Сумма чисел от 1 до N
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = 5
print(f'Сумма чисел от 1 до {n}: {sum_numbers(n)}\n')

# Задача 2: Поиск минимального числа в списке
def find_min(numbers):
    min_num = numbers[0]  # Начинаем с первого элемента
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

numbers = [3, 1, 4, 1, 5]
print(f'Минимальное число в списке {numbers}: {find_min(numbers)}\n')

# Задача 3: Подсчёт гласных в строке
def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

text = 'Hello World'
print(f'Количество гласных в строке "{text}": {count_vowels(text)}\n')

# Задача 4: Ромбовидный треугольник
def print_diamond(rows):
    for i in range(1, rows + 1):
        print('*' * i)

    for i in range(rows - 1, 0, -1):
        print('*' * i)

print_diamond(4)

# Задача 5: Обратный отсчёт
def countdown():
    for i in range(10, 0, -1):
        print(i)
    print('Старт!\n')

print('')
countdown()

# Задача 6: Обратный отсчёт - 2
def countdown():
    number = 10
    while number > 0:
        print(number)
        number -= 1
    print('Старт!')

countdown()