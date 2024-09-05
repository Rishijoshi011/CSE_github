import re 

# ! 1.1:- Write a Python Program that searches a string to see if it starts with "The" and ends with "Indus".

str = "The abcd Indus"
pattern = re.compile("^The.*Indus$")

if re.search(pattern, str):
    print("Match found")
else:
    print("Match not found")    

# match = re.search(pattern, str)
# if match:
#     print("Match found", match.group())
# else:
#     print("Match not found")  

# ! 1.2 :- Write a Python Program that returns a match where the string contains a white space character.

str2 = "This is a string with some whitespace"
pattern2 = re.compile(" ")

if re.findall(pattern2, str2):
    print("White space found")
else:
    print("White space not found")    

# match2 = re.findall(pattern2, str2)
# if match2:
#     print("White space found", match2)
# else:
#     print("White space not found")


# ! 1.3: Write a Python program that matches a string that has an a followed by three 'b'.

str3 = "hello therebbb test stringbbb"
pattern3 = re.compile(r"bbb")

match3 = re.finditer(pattern3, str3)
if match3:
    print("words found", list(match3))
else:
    print("words not found")


# ! 1.4:- Write a Regular Expression to find Words or strings having three characters and with ‘m’ as first character

