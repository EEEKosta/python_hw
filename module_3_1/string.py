import re
# Строки - задачи https://shining-belly-95d.notion.site/1afd2c43f99880bc8b85fc84747c1982
# Задача 1: Анаграмма
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram('listen', 'silent'))
print(is_anagram('hello', 'world'), '\n')

# Задача 2: Палиндром
def is_palindrome(s):
    clean = re.sub(r'[^A-Za-z]', '', s)
    return clean.lower() == clean[::-1].lower()

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"), '\n')

# Задача 3: Самое длинное слово
def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest

text = "In the middle of a vast desert, an extraordinary adventure awaits"
print(longest_word(text), '\n')

# Задача 4: Форматирование номера телефона
def format_phone_number(digits):
    area = digits[0:3]
    prefix = digits[3:6]
    line = digits[6:10]
    return f'({area}) {prefix}-{line}'

print(format_phone_number("1234567890"), '\n')

# Задача 5: Удаление дублирующих символов
def remove_duplicates(s):
    result = ''
    for char in s:
        if char not in result:
            result += char
    return result

print(remove_duplicates("programming"), '\n')

# Задача 6: Проверка на уникальность символов
def is_unique(s):
    return len(s) == len(set(s))

print(is_unique("abcdef"))
print(is_unique("hello"))