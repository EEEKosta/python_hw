# 6. Коллекции данных
bugs = [
    "Ошибка 1 — Hi",
    "Ошибка 2 — Low",
    "Ошибка 3 — Mid",
    "Ошибка 4 — low",
    "Ошибка 5 — High"
]

priority_bugs = {
    'high': 0,
    'mid': 1,
    'low': 2
}

def bug_append():
    bugs.append(input('Введите баг: '))

bug_append()

def bug_remove():
    bug_num = int(input('Введите номер бага для удаления:'))
    del bugs[bug_num]

bug_remove()

def get_priority(bug):
    parts = bug.split('—')
    if len(parts) > 1:
        priority = parts[1].strip().lower()
        return priority_bugs.get(priority, 999)
    return 999

sorted_bugs = sorted(bugs, key=get_priority)

for bug in sorted_bugs:
    print(bug)

