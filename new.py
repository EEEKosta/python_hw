def dict_to_lists(my_dict):
    return list(my_dict.keys()), list(my_dict.values())


my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict), "\n")  # (['a', 'b', 'c'], [1, 2, 3])

print(my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
