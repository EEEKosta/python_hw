# Списки - задачи https://shining-belly-95d.notion.site/1afd2c43f99880f3b89af5bd6ddae651
# Задача 1: Удаление дубликатов
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4]), '\n')

# Задача 2: Генерация списка квадратов
def generate_squares(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

print(generate_squares(5), '\n')

# Задача 3: Объединение двух списков
def merge_lists(list1, list2):
    merged_set = list1 + list2
    return list(set(merged_set))

print(merge_lists([1, 2, 3], [3, 4, 5]), '\n')

# Задача 4: Проверка на отсортированность
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]), '\n')

# Задача 5: Слияние списков
def merge_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]