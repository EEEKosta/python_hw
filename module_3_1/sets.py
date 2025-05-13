# https://shining-belly-95d.notion.site/1afd2c43f998807689fad3afbd8e21dc
# Множества - задачи
# Задача 1: Уникальные элементы списка
def get_unique_elements(lst):
    return list(set(lst))


print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]), "\n")  # [1, 2, 3, 4, 5]


# Задача 2: Проверка списка на уникальность элементов
def is_unique_list(lst):
    return len(lst) == len(set(lst))


print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]), "\n")  # False


# Задача 3: Получение уникальных гласных из строки
def get_unique_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {char for char in s.lower() if char in vowels}


print(get_unique_vowels("Hello World"))  # {'e', 'o'}
