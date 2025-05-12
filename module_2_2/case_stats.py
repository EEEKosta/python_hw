# 5. Операции с данными
def case_stat():
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    case_counts = []

    for day in days:
        while True:
                count = int(input(f"Введите количество тест-кейсов за {day}: "))
                case_counts.append(count)
                break

    total = sum(case_counts)
    average = total / len(days)

    print(f"Общее количество тестов за неделю: {total}")
    print(f"Среднее количество тестов в день: {average}")

    if average > 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")

case_stat()