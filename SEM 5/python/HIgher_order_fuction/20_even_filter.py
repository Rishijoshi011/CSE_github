
# TODO: find if number is even using filter

size = int(input("Enter size of an List: "))
numbers = []

print("Enter Elements: ")
for i in range(size):
    numbers.append(int(input()))

def isEven(x):
    if(x % 2 == 0):
        return True

result = filter(isEven, numbers)
    
print(list(result))