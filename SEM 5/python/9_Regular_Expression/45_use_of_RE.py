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

# ! 1.7:- Write a regular expression to retrieve all words having 5 character length.

str7 = "hello test msg from user1 says abcde"
pattern7 = r"\b\w{5}\b"

match7 = re.findall(pattern7, str7)
if match7:
    print("5 length words:", match7)
else:
    print("5 length words not found")

# ! 1.8: Write a regular expression to retrieve all words with 3,4 or 5 character length.

str8 = "hello test message from a user1 says ab"
pattern8 = r"\b\w{3,5}\b"

match8 = re.findall(pattern8, str8)
if match8:
    print("3 to 5 length words:", match8)
else:
    print("3 to 5 length words not found")

# ! 1.9:- Write a regular expression to retrieve all single digits from a string.

str9 = "hello test 40 4 message from a user 1 says ab"
pattern9 = r"\b\d{1}\b"

match9 = re.findall(pattern9, str9)
if match9:
    print("single dig:", match9)
else:
    print("single dig not found")


# ! 1.10:- Write a regular expression to retrieve the last word from the string.

str10 = "hello test msg from a user 1 says ab"
pattern10 = r"\b\w+$"

match10 = re.findall(pattern10, str10)
if match10:
    print("Last string:", match10)
else:
    print("String is empty")

# ! 1.11:- Write a regular expression to retrieve all words starting with ‘an’ or ‘ak’.

str11 = "hello aktest msg from a anna says ab"
pattern11 = r"\bak\w*|an\w*\b"

match11 = re.findall(pattern11, str11)
if match11:
    print("an or ak:", match11)
else:
    print("not found")

# ! 1.12:- Write a regular expression to retrieve DOB from the string.

str12 = "my birthdate 31-02-1960"
pattern12 = r"\d{1,2}-\d{1,2}-\d{4}"

match12 = re.findall(pattern12, str12)
if match12:
    print("DOB:", match12)
else:
    print("DOB not found")
