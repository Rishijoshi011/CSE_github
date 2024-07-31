
user_input = input("Enter a sequence of comma-separated numbers: ")
number_strings = user_input.split(',')

numbers_list = [int(num) for num in number_strings]
numbers_tuple = tuple(numbers_list)

print("List of numbers:", numbers_list)
print("Tuple of numbers:", numbers_tuple)
