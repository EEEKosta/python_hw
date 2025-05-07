# 4.1. Fullstack. Функции, управляющие конструкции
# 5. Работа с вложенными функциями

def calculator():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    operation = input('Выберите операцию (+, -, *, /): ')

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return 'Ошибка: деление на ноль'
        return x / y

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        return 'Ошибка: неизвестная операция'

    print(f'Результат: {result}')


calculator()

'''
Напишите программу, которая:
Реализует основную функцию calculator(), которая:
Спрашивает у пользователя два числа.
Спрашивает операцию (+, , , /).
Использует вложенные функции для выполнения каждой операции.
Возвращает результат выбранной операции.

Пример работы программы:
Введите первое число: 10
Введите второе число: 5
Выберите операцию (+, -, *, /): *
Результат: 50
'''