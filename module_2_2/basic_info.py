# 3. Основы
name = input("Введите ваше имя: ")
exp_on_qa = input("сколько лет работаешь в QA: ")

if name and exp_on_qa:
    print(f"Привет, {name}! Добро пожаловать в мир Python для тестировщиков.")

    while True:
        var = input("Что такое переменная: ")
        if var == 'то се':
            print('Верно')
            break
        else:
            print('не верно, попробуй еще раз')

else:
    print('Введи имя и опыт')