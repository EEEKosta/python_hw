# 7. Изменяемые и неизменяемые типы данных
def bug_info():
    id = int(input('введите id бага: '))
    name = input('введите имя бага: ')
    status = input('введите статус бага: ')

    bug = {
        'ID': id,
        'name': name,
        'status': status
    }

    print(bug)

bug_info()