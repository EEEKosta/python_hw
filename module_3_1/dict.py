# https://shining-belly-95d.notion.site/1afd2c43f998801fbaa3ca21cb1d126c
# Словари - задачи
# Задача 1: Частотный анализ строки
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


print(char_frequency("hello"), "\n") # {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# Задача 2: Слияние двух словарей
def merge_dicts(dict1, dict2):
    result = dict1
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2), "\n") # {'a': 1, 'b': 5, 'c': 4}


# Задача 3: Обратное преобразование словаря в два списка
def dict_to_lists(my_dict):
    return list(my_dict.keys()), list(my_dict.values())


my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict), "\n")  # (["a", "b", "c"], [1, 2, 3])


# Задача 4: Группировка элементов по первому символу
def group_by_first_letter(strings):
    result = {}
    for word in strings:
        first_letter = word[0]
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]
    return result


strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings), "\n")
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}


# Задача 5: Извлечение подсловаря
def extract_subdict(my_dict, keys):
    return {key: my_dict[key] for key in keys if key in my_dict}


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys)) # {"a": 1, "c": 3}
