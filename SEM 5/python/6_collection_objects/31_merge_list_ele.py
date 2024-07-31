
# TODO: Merge all elements into a single string

words = []
str = ""
print("Enter Words: ")
for i in range(5):
    words.append(input())
    str += words[i] # * concatenating in same loop and removing need of second loop


print(f"Whole String: {str}")