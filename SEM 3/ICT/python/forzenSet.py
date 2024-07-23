# # dogs = {"pitbull", "husky", "golden"}
# # choosenDogs = frozenset(dogs)

# # print(dogs)
# # print(choosenDogs)

# # dogs.add("german shepherd")
# # print(dogs)
# # # choosenDogs.add("german shepherd") it wil give you error 

# # List
# my_list = [1, 2, 3]
# my_list[0] = 4  # Lists are mutable, you can change elements
# print(my_list)  # Output: [4, 2, 3]

# # Tuple
# my_tuple = (1, 2, 3)
# # my_tuple[0] = 4  # This would raise an error, tuples are immutable
# print(my_tuple)


# Set
my_set = {1, 2, 3}
my_set.add(4)  # Sets are mutable, you can add and remove elements
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict['key3'] = 'value3'  # Dictionaries are mutable, you can add, remove, and modify key-value pairs
del my_dict['key2']
print(my_dict)  # Output: {'key1': 'value1', 'key3': 'value3'}
