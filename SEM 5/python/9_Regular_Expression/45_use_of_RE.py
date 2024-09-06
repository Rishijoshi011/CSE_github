import re 

# ! 1.1:- Write a Python Program that searches a string to see if it starts with "The" and ends with "Indus".

str = "The abcd Indus"
pattern = r"^The.*Indus$"

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
pattern2 = r" "

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
pattern3 = r"\w+[bbb]\b"

match3 = re.findall(pattern3, str3)
if match3:
    print("Match found:", match3)
else:
    print("Match not found")



# ! 1.4:- Write a Regular Expression to find Words or strings having three characters and with ‘m’ as first character

str4 = "hello mmmthis is mmmtest msg"
pattern4 = r"\bmmm\w+"

match4 = re.findall(pattern4, str4)
if match4:
    print("Format found:", match4)
else:
    print("Format not found")


# ! 1.5:- Write a regular expression to retrieve all words starting with “a”.

str5 = "hello abc test astring"
pattern5 = r"\b[a]\w+"

match5 = re.findall(pattern5, str5)
if match5:
    print("Str with a:", match5)
else:
    print("Str with not a found")

# ! 1.6:- Write a regular expression to retrieve all words starting with a numeric digit.

str6 = "hello 123test 567data from 345t"
pattern6 = r"\b[\d]\w+"
match6 = re.findall(pattern6, str6)
if match6:
    print("Digits:", match6)
else:
    print("Numeric not found")

# ! 1.7:-     
