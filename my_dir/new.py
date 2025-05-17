# def dict_to_lists(my_dict):
#     return list(my_dict.keys()), list(my_dict.values())
#
#
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(dict_to_lists(my_dict), "\n")  # (['a', 'b', 'c'], [1, 2, 3])
#
# print(my_dict)
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())


lst = [
  {
    "bookingid": 295
  },
  {
    "bookingid": 349
  },
  {
    "bookingid": 173
  },
  {
    "bookingid": 448
  }
]

assert any(item["bookingid"] == 295 for item in lst)

# print(len(lst))
# print(lst[0]["bookingid"])
# print(any(item["bookingid"] == 295 for item in lst))