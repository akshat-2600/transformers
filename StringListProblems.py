# String Based Assignment Problem
'''Q1 Write a program to reverse a string.'''

s = input("Enter a string :")
reverse_string=s[::-1]
print("Reversed string is ",reverse_string)
Reversed string is  .anexaS tahskA si eman yM
'''Q2 Check if a string is a palindrome.'''

k = input("Enter a string :")
removed_whitespaces = k.replace(" ", "").lower()
reversed = removed_whitespaces[::-1]
if reversed == removed_whitespaces:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
The input string is not a palindrome.
'''Q3 Convert a string to uppercase.'''

a = input("Enter a string :")
uppercase_string = a.upper()
print("Uppercase string is ",uppercase_string)
Uppercase string is  MY NAME IS AKSHAT SAXENA.
'''Q4 Convert a string to lowercase.'''

a = input("Enter a string :")
lowercase_string = a.lower()
print("Lowercase string is ",lowercase_string)
Lowercase string is  my name is akshat saxena.
'''Q5 Count the number of vowels in a string.'''

b = input("Enter a string :")
vowels = b.count("A") + b.count("E") + b.count("I") + b.count("O") + b.count("U") + b.count("a") + b.count("e") + b.count("i") + b.count("o") + b.count("u")
print("Number of vowels in string provided is ",vowels)
Number of vowels in string provided is  8
'''Q6 Count the number of consonants in a string.'''

consonant = 0
s = input("Enter a string :")
length = len(s)
v = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
for i in range(length):
    if s[i] in v:
        consonant += 1
print("Number of consonants in string provided is ",consonant)
Number of consonants in string provided is  12
'''Q7 Remove all whitespaces from a string.'''

string = input("Enter a string :")
modified_string = ""
for i in string:
    if i != " ":
        modified_string += i
print("Modified string without spaces is ",modified_string)
Modified string without spaces is  MynameisAkshatSaxena.
'''Q8 Find the length of a string without using the `len()` function.'''

count = 0
string = input("Enter a string :")
for i in string:
    count += 1
print("Length of string provided is ",count)
Length of string provided is  25
'''Q9 Check if a string contains a specific word.'''

string = input("Enter a string :")
word = input("Enter the specific word to be checked :")
if word in string:
    print(word ,"is present in string")
else:
    print(word ,"is not present in string")
IS is not present in string
'''Q10 Replace a word in a string with another word.'''

string = input("Enter a string :")
word = input("Enter the specific word to be replaced :")
new_word = input("Enter the new word :")
replace_string = string.replace(word , new_word)
print("New string with replaced word is ",replace_string)
New string with replaced word is  Today is Monday.
'''Q11 Count the occurrences of a word in a string.'''

word_count = 0
string = input("Enter a string :")
word = input("Enter the word to be counted :")
f = string.split()
for i in range(len(f)):
    if word == f[i]:
        word_count += 1    
print("The occurances of", word ,"in string provided is",word_count)
The occurances of school in string provided is 1
'''Q12 Find the first occurrence of a word in a string.'''

string = input("Enter a string :")
word = input("Enter the word to be searched :")
o = string.find(word)
if o == -1:
    print("Entered word is not in string")
else:
    print("The first occurance of" ,word ,"is" ,o)
The first occurance of Akshat is 11
'''Q13 Find the last occurrence of a word in a string.'''

string = input("Enter a string :")
length = len(string)
word = input("Enter the word to be searched :")
reverse_string = string[::-1]
l = reverse_string.find(word[::-1])
if l == -1:
    print("Entered word is not in string")
else:
    print("The last occurance of" ,word ,"is" ,length - l -len(word))
The last occurance of Hello is 6
'''Q14 Split a string into a list of words.'''

string = input("Enter a string :")
word_split = input("Enter the word to split the string on :")
l = string.split(word_split)
print("Splitted string is ",l)
Splitted string is  ['My', 'name', 'is', 'Akshat', 'Saxena', '.']
'''Q15 Join a list of words into a string.'''

list_of_words = eval(input("Enter list of words :"))
joined = ' '.join(list_of_words)
print("Joined list of words into a string is ",joined)
Joined list of words into a string is  I study in PW SKILLS
'''Q16 Convert a string where words are separated by spaces to one where words
are separated by underscores.'''

string = input("Enter a string separated by spaces :")
print("String separated by spaces is ",string)
underscore = string.replace(" ","_")
print("String separated by underscores is ",underscore)
String separated by spaces is  My name is Akshat Saxena .
String separated by underscores is  My_name_is_Akshat_Saxena_.
'''Q17 Check if a string starts with a specific word or phrase.'''

string = input("Enter a string :")
word = input("Enter a word or phrase :")
check = string.startswith(word)
if check == True:
    print("The string starts with ", word)
else:
    print("The string does not starts with ", word)
The string does not starts with  study
'''Q18 Check if a string ends with a specific word or phrase.'''

string = input("Enter a string :")
word = input("Enter a word or phrase :")
check = string.endswith(word)
if check == True:
    print("The string ends with ", word)
else:
    print("The string does not ends with ", word)
The string ends with  PW SKILLS
'''Q19 Convert a string to title case (e.g., "hello world" to "Hello World").'''

string = input("Enter a string :")
t = string.title()
print("Title cased string is",t)
Title cased string is I Study In Pw Skills
'''Q20 Find the longest word in a string.'''

string = input("Enter a string :")
L =[]
k = string.split()
for i in range(len(k)):
    L.append(len(k[i]))
    max_num = max(L)
    index_word = L.index(max_num)
print("The longest word in the string provided is", k[index_word])
The longest word in the string provided is Akshat
'''Q21 Find the shortest word in a string.'''

string = input("Enter a string :")
L =[]
k = string.split()
for i in range(len(k)):
    L.append(len(k[i]))
    min_num = min(L)
    index_word = L.index(min_num)
print("The shortest word in the string provided is", k[index_word])
The shortest word in the string provided is I
'''Q22 Reverse the order of words in a string.'''

string = input("Enter a string :")
reverse_string = ""
k = string.split()
for i in k :
    reverse_string += i[::-1]
    reverse_string += " "
print("String after reversing the order of words is", reverse_string)
String after reversing the order of words is yM eman si tahskA anexaS . 
'''Q23 Check if a string is alphanumeric.'''

string = input("Enter a string :")
check = string.isalnum()
if check:
    print("String is alphanumeric")
else:
    print("String is not alphanumeric")
String is not alphanumeric
'''Q24 Extract all digits from a string.'''

string = input("Enter a string :")
digit = " "
for i in string :
    if i.isdigit() :
        digit += i
print("Extracted digits from string are", digit) 
Extracted digits from string are  1812
'''Q25 Extract all alphabets from a string.'''

string = input("Enter a string :")
alphabets = " "
for i in string :
    if i.isalpha() :
        alphabets += i
print("Extracted alphabets from string are", alphabets)
Extracted alphabets from string are  IamyearsoldIstudyinclassth
'''Q26 Count the number of uppercase letters in a string.'''

string = input("Enter a string :")
count = 0
for i in string :
    if i.isupper() :
        count += 1
print("The number of uppercase letters in the string are", count)
The number of uppercase letters in the string are 3
'''Q27 Count the number of lowercase letters in a string.'''

string = input("Enter a string :")
count = 0
for i in string :
    if i.islower() :
        count += 1
print("The number of lowercase letters in the string are", count)
The number of lowercase letters in the string are 17
'''Q28 Swap the case of each character in a string.'''

string = input("Enter a string :")
new_string = ""
for i in string :
    new_string += i.swapcase()
print("Swapped case string is", new_string)
Swapped case string is mY NAME IS aKSHAT sAXENA .
'''Q29 Remove a specific word from a string.'''

string = input("Enter a string :")
new_string = ""
a = True
while a :
    word = input("Enter a word to be removed :")
    if word in string.split() :
        a = False
    else :
        print("Enter valid word to be removed")
s = string.split()
for i in s :
    if i != word :
        new_string += i
        new_string += " "
print("String after removing specific word is", new_string)
Enter valid word to be removed
Enter valid word to be removed
String after removing specific word is My name is Saxena . 
'''Q30 Check if a string is a valid email address.'''

import re

def check_valid_email(email) :
    regular_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(regular_pattern , email) :
        return "valid email"
    else :
        return "invalid email"

email_1 = "hello@email.com"
email_2 = "invalid*email"
output_1 = check_valid_email(email_1)
output_2 = check_valid_email(email_2)
print("email_1 is ", output_1)
print("email_2 is ", output_2)
email_1 is  valid email
email_2 is  invalid email
'''Q31 Extract the username from an email address string.'''


def extract_username(e):
    u = e.split("@")[0]
    return u

email = input("Enter a email address :")
username = extract_username(email)
print("Username is ", username)
Username is  akshat
'''Q32 Extract the domain name from an email address string.'''

def extract_domain_name(e):
    d = e.split("@")[1]
    return d

email = input("Enter a email address :")
domain_name = extract_domain_name(email)
print("Domain name is ", domain_name)
Domain name is  email.com
'''Q33 Replace multiple spaces in a string with a single space.'''

def replace_multiple_spaces(s) :
    new_string = " ".join(s.split())
    return new_string
    
string = input("Enter a string :") # "  akshat hello    how  are you    "
output = replace_multiple_spaces(string)
print("String after replacing multiple spaces is ",output)          
String after replacing multiple spaces is  akshat hello how are you
'''Q34 Check if a string is a valid URL.'''

from urllib.parse import urlparse
def check_valid_url(url):
    try :
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError :
        return False

url_1 = "https://www.youtube.com/"
url_2 = "invalid*url"
output_1 = check_valid_url(url_1)
output_2 = check_valid_url(url_2)
print("url_1 is ", output_1)
print("url_2 is ", output_2)
url_1 is  True
url_2 is  False
'''Q35 Extract the protocol (http or https) from a URL string.'''

def extract_protocol(url) :
    index = url.find("://")
    if index != -1 :
        return url[:index]
    else :
        return "No protocol"
            
url_1 = input("Enter 1st url :")
url_2 = input("Enter 2nd url :")
url_3 = input("Enter 3rd url :")

protocol_1 = extract_protocol(url_1)
protocol_2 = extract_protocol(url_2)
protocol_3 = extract_protocol(url_3)

print("Protocol 1 is ",protocol_1)
print("Protocol 2 is ",protocol_2)
print("Protocol 3 is ",protocol_3)
Protocol 1 is  http
Protocol 2 is  ftp
Protocol 3 is  https
'''Q36 Find the frequency of each character in a string.'''

string = input("Enter a string :")
new_string = ""
dictionary = {}
for i in string :
    if i not in new_string :
        dictionary[i] = 1
        new_string += i
    else :
        dictionary.update({i : dictionary[i] + 1})
for i , k in dictionary.items() :
    print("Frequency of ", i ,":" , k)
Frequency of  h : 1
Frequency of  e : 1
Frequency of  l : 3
Frequency of  o : 2
Frequency of  w : 1
Frequency of  r : 1
Frequency of  d : 1
'''Q37 Remove all punctuation from a string.'''

import string
def remove_puntuations(input_string) :
    translator = str.maketrans("","",string.punctuation)
    clean_string = input_string.translate(translator)
    return clean_string
    
input_string = input("Enter a string :")
cleaned_string = remove_puntuations(input_string)
print("Original string :",input_string)
print("Cleaned string :",cleaned_string)
Original string : Hello, Rahul! What's up?
Cleaned string : Hello Rahul Whats up
'''Q38 Check if a string contains only digits.'''

string = input("Enter a string :")
if string.isdigit() :
    print("String contains only digits")
else :
    print("String does not contains only digits")
String contains only digits
'''Q39 Check if a string contains only alphabets.'''

string = input("Enter a string :")
if string.isalpha() :
    print("String contains only alphabets")
else :
    print("String does not contains only alphabets")
String does not contains only alphabets
'''Q40 Convert a string to a list of characters.'''

string = input("Enter a string :")
convert = list(string)
print("Converted string to a list of characters :",convert)
Converted string to a list of characters : ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'A', 'k', 's', 'h', 'a', 't', ' ', 'S', 'a', 'x', 'e', 'n', 'a', ' ', '.']
''' Q41 Check if two strings are anagrams.'''

string_1 = input("Enter 1st string :") #worth
string_2 = input("Enter 2nd string :") #throw
new_string1 = ""
new_string2 = ""
dictionary_1 = {}
dictionary_2 = {}

#Checking 1st string
for i in string_1 :
    if i not in new_string1 :
        dictionary_1[i] = 1
        new_string1 += i
    else :
        dictionary_1.update({i : dictionary_1[i] + 1})
        
#Checking 2nd string
for i in string_2 :
    if i not in new_string2 :
        dictionary_2[i] = 1
        new_string2 += i
    else :
        dictionary_2.update({i : dictionary_2[i] + 1})
        
#Comparing both dictionaries
if dictionary_1 == dictionary_2 :
    print("Both strings are amagrams")
else :
    print("Bothe strings are not amagrams")
Both strings are amagrams
'''Q42 Encode a string using a Caesar cipher.'''

#defining function Caesar_cipher
def Caesar_cipher(text , shift) :
    encoded_text = ""
    for char in text :
        if char.isalpha() :
            encoded_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else :
            encode_char = char
        
        encoded_text += encoded_char
    
    return encoded_text
    
#Defining the input text and shift value for encoding
string = input("Enter a string to encode :")
shift = int(input("Enter shift value for encoding :"))

#Calling function Caesar_cipher
encoded_text = Caesar_cipher(string , shift)
            
#Printing the encoded text
print("Encoded text :", encoded_text)
Encoded text : wmujcvvoczgpc
'''Q43 Decode a Caesar cipher encoded string.'''

#Defining function Caesar_cipher_decode
def Caesar_cipher_decode(text , shift) :
    decoded_text = ""
    for char in text :
        if char.isalpha() :
            decoded_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else :
            decoded_char = char
        
        decoded_text += decoded_char
        
    return decoded_text


#defining input text and shift value for decoding
string = input("Enter a string to decode :")
shift = int(input("Enter shift value for decoding :"))

#Calling function Caesar_cipher_decode
decoded_text = Caesar_cipher_decode(string , shift)

#Printing the decoded text
print("Decoded text :", decoded_text)
Decoded text : fcjjm fmu ypc wms
'''Q44 Find the most frequent word in a string.'''

string = input("Enter a string :")
arrange_words = string.split()
frequency = {}
for i in arrange_words :
    if i in frequency :
        frequency[i] += 1
    else :
        frequency[i] = 1

frequent = max(frequency.values())
for i in frequency :
    if frequency[i] == frequent :
        print("Most frequent word is ", i ," with ", frequent ,"times repetition")  
Most frequent word is  world  with  3 times repetition
'''Q45 Find all unique words in a string.'''

string = input("Enter a string :")
arrange_words = string.split()
unique_words = set()
for i in arrange_words :
    unique_words.add(i)
    
print("All unique words in string are :")
for i in unique_words :
    print(i)
All unique words in string are :
felt
the
feel
others
were
really
saw
because
happy,
wasn't
and
but
happy.
I
knew
happy
should
'''Q46 Count the number of syllables in a string.'''

def syllables(string) :
    arrange_words = string.split()
    count = 0
    for word in arrange_words :
        for char in word :
            if char in ["a","e","i","o","u","A","E","I","O","U"] :
                count += 1
    return count
string1 = input("Enter 1st string :")
string2 = input("Enter 2nd string :")

syllable_1 = syllables(string1)
syllable_2 = syllables(string2)


print("The number of syllables in the", string1, " are ", syllable_1)
print("The number of syllables in the ", string2, "are  ", syllable_2) 
The number of syllables in the Mat  are  1
The number of syllables in the  Game are   2
'''Q47 Check if a string contains any special characters.'''

import re

def check_special_characters(string) :
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/]')
    match = pattern.search(string)
    return bool(match)

string_1 = input("Enter 1st string :")
string_2 = input("Enter 2nd string :")

result_1 = check_special_characters(string_1)
result_2 = check_special_characters(string_2)

print(f"'{string_1}' contains special characters:", result_1)
print(f"'{string_2}' contains special characters:", result_2)
'Hello! How are you?' contains special characters: True
'Let's go! It's showtime .' contains special characters: True
'''Q48 Remove the nth word from a string.'''

string = input("Enter a string :")
nth_value = int(input("Enter nth word to be removed :"))
arrange_words = string.split()
if nth_value >=1 and nth_value <= len(arrange_words) :
    removed_word = arrange_words.pop(nth_value-1)
    cleaned_string = " ".join(arrange_words)
print("Original string :", string)
print("Cleaned string :", cleaned_string)
print("Removed word :", removed_word)
Original string : Please bring your books with you to every class.
Cleaned string : Please bring books with you to every class.
Removed word : your
'''Q49 Insert a word at the nth position in a string.'''

string = input("Enter a string :")
nth_value = int(input("Enter nth value to insert word :"))
word = input("Enter word to be inserted :")
arrange_words = string.split()
if nth_value >=1 and nth_value <= len(arrange_words) :
    arrange_words.insert(nth_value - 1 , word)
    cleaned_string = " ".join(arrange_words)
print("Original string :", string)
print("Cleaned string :", cleaned_string)
Original string : Please bring books with you to every class.
Cleaned string : Please bring your books with you to every class.
'''Q50 Convert a CSV string to a list of lists.'''

def csv_string_list(string) :
    new_list = []
    lines = string.split("\n")
    for line in lines:
        fields = line.split(",")
        new_list.append(fields)

    return new_list

string = "Roll No., Name, Marks\n01, Rahul, 79\n02, Sonu, 89"
list_of_lists = csv_string_list(string)

for row in list_of_lists :
    print(row)
['Roll No.', ' Name', ' Marks']
['01', ' Rahul', ' 79']
['02', ' Sonu', ' 89']
 
# List based practice problem 
'''Q1 Create a list with integers from 1 to 10.'''

lst = []
for i in range(1,11) :
    lst.append(i)
print(lst)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''Q2 Find the length of a list without using the `len()` function.'''

lst = eval(input("Enter a list :"))
count = 0
for i in lst :
    count += 1
print("Length of list provided :", count)
Length of list provided : 6
'''Q3 Append an element to the end of a list. '''

lst = eval(input("Enter a list :"))
element = int(input("Enter a element to be appended :"))
lst.append(element)
print("List after updation :", lst)
List after updation : [1, 3, 5, 7, 9, 11, 13]
'''Q4 Insert an element at a specific index in a list.'''

lst = eval(input("Enter a list :"))
element = int(input("Enter a element to be inserted :"))
index = int(input("Enter index to insert element :"))
lst.insert(index , element)
print("List after updation :", lst)
List after updation : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''Q5 Remove an element from a list by its value.'''

lst = eval(input("Enter a list :"))
element = eval(input("Enter element to be removed :"))
lst.remove(element)
print("List after updation :",lst)
List after updation : [2, 4, 6, 8, 10, 12]
'''Q6 Remove an element from a list by its index.'''

lst = eval(input("Enter a list :"))
index = int(input("Enter index of element to be removed :"))
lst.pop(index)
print("List after updation :",lst)
List after updation : [1, 3, 5, 7, 9, 11]
'''Q7 Check if an element exists in a list.'''

lst = eval(input("Enter a list :"))
element = eval(input("Enter element to check it's existence in list :"))
if element in lst :
    print(element ,"exists in list")
else :
    print(element ,"does not exist in list")
7 exists in list
'''Q8 Find the index of the first occurrence of an element in a list.'''

lst = eval(input("Enter a list :"))
element = eval(input("Enter element to find it's index :"))
index = lst.index(element)
print(f"index of {element} : {index}")
index of game : 3
'''Q9 Count the occurrences of an element in a list.'''

lst = eval(input("Enter a list :"))
element = eval(input("Enter element to count it's number of occurence :"))
count = lst.count(element)
print(f"Number of occurence of {element} : {count}")
Number of occurence of game : 2
''' Q10 Reverse the order of elements in a list.'''

lst = eval(input("Enter a list :"))
lst.reverse()
print(f"Reversed list {lst}")
Reversed list ['hi', 'game', 'skills', 'saxena', 'akshat', 'game', 'wallah', 'skills', 'pw']
'''Q11 Sort a list in ascending order.'''

lst = eval(input("Enter a list :"))
lst.sort()
print(f"List in ascending order : {lst}")
List in ascending order : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''Q12 Sort a list in descending order.'''

lst = eval(input("Enter a list :"))
lst.sort(reverse=True)
print(f"List in ascending order : {lst}")
List in ascending order : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''Q13 Create a list of even numbers from 1 to 20.'''

lst = []
for i in range(1,21) :
    if i%2 == 0 :
        lst.append(i)
print("List of even numbers from 1 to 20 :", lst)
List of even numbers from 1 to 20 : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''Q14 Create a list of odd numbers from 1 to 20.'''

lst = []
for i in range(1,21) :
    if i%2 != 0 :
        lst.append(i)
print("List of odd numbers from 1 to 20 :", lst)
List of odd numbers from 1 to 20 : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
'''Q15 Find the sum of all elements in a list.'''

from functools import reduce 

sum = 0
lst = eval(input("Enter a list :"))
sum_element = reduce(lambda a,b : a + b , lst)
print("Sum of all elements of list :", sum_element)
Sum of all elements of list : 55
'''Q16 Find the maximum value in a list.'''

lst = eval(input("Enter a list :"))
max_value = max(lst)
print("Maximum value in ", lst ,":", max_value)
Maximum value in  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] : 10
'''Q17 Find the minimum value in a list.'''

lst = eval(input("Enter a list :"))
min_value = min(lst)
print("Minimum value in ", lst ,":", min_value)
Minimum value in  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] : 1
'''Q18 Create a list of squares of numbers from 1 to 10.'''

lst = eval(input("Enter a list from 1 to 10 :"))
squares_list = list(map(lambda i : i**2 , lst))
print("List of squares of numbers from 1 to 10 :", squares_list)
List of squares of numbers from 1 to 10 : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''Q19 Create a list of random numbers.'''

import random

lst =[]
for i in range(10) :
    lst += [random.randint(1,1001)]
print("List of random numbers :",lst)
List of random numbers : [40, 706, 801, 52, 341, 633, 161, 158, 35, 88]
'''Q20 Remove duplicates from a list.'''

s = set()
lst = eval(input("Enter a list with duplicate elements :"))
for i in lst :
    s.add(i)
print("List with duplicate elements removed :", list(s))
List with duplicate elements removed : [1, 2, 3, 4, 5, 6, 7, 8]
'''Q21 Find the common elements between two lists.'''

lst_1 = eval(input("Enter 1st list :"))
lst_2 = eval(input("Enter 2nd list :"))
new_lst = []
print("Common elements between two lists :")
for i in lst_1 :
    for j in lst_2 :
        if i == j :
            if i in new_lst :
                continue
            else :
                new_lst.append(i)
if len(new_lst) == 0 :
    print("No element is common")
for i in new_lst :
    print(i)
Common elements between two lists :
4
6
26
'''Q22 Find the difference between two lists.'''

lst_1 = eval(input("Enter 1st list :"))
lst_2 = eval(input("Enter 2nd list :"))
difference = list(set(lst_1).difference(lst_2))
print("Difference between both list :", difference)
Difference between both list : ['Tokyo', 'Paris']
'''Q23 Merge two lists.'''

lst_1 = eval(input("Enter 1st list :"))
lst_2 = eval(input("Enter 2nd list :"))
merge_lst = lst_1 + lst_2
print("New list after merging to lists :", merge_lst)
New list after merging to lists : ['Tokyo', 'Berlin', 'Paris', 'Rio', 'Berlin', 'India', 'Rio']
'''Q24 Multiply all elements in a list by 2.'''

lst = eval(input("Enter a list :"))
new_list = list(map(lambda i : i*2 , lst))
print("List after multiplying all elements by 2 :", new_list)
List after multiplying all elements by 2 : ['TokyoTokyo', 'BerlinBerlin', 'ParisParis', 'RioRio']
'''Q25 Filter out all even numbers from a list.'''

lst = eval(input("Enter a list which contains numbers :"))
even_lst = list(filter(lambda i : i%2 == 0 , lst))
print("All even numbers in list :", even_lst)
All even numbers in list : [2, 8, 10, 36, 50, 4]
'''Q26 Convert a list of strings to a list of integers.'''

lst = eval(input("Enter a list of strings :"))
integer_lst = list(map(lambda i : int(i) , lst))
print("List of integers :", integer_lst)
List of integers : [10, 30, 2, 5]
'''Q27 Convert a list of integers to a list of strings.'''

lst = eval(input("Enter a list of integers :"))
string_lst = list(map(lambda i : str(i) , lst))
print("List of strings :", string_lst)
List of strings : ['10', '30', '2', '5']
'''Q28 Flatten a nested list.'''

nested_lst = eval(input("Enter a nested list :"))
flatten_lst = []
for lst in nested_lst :
    if type(lst) != type([]) :
        flatten_lst.append(lst)
        continue
    for element in lst :
        flatten_lst.append(element)
print("Flattened nested list :", flatten_lst)
Flattened nested list : [2, 3, 4, 6, 7, 9, 10, 8, 12, 14]
'''Q29 Create a list of the first 10 Fibonacci numbers.'''

def fib_num(n) :
    lst = [0,1]
    for i in range(2,n) :
        next_fib_num = lst[i-1] + lst[i-2]
        lst.append(next_fib_num)
    return lst

n = int(input("Enter number of fibnacci numbers you want :"))
lst = fib_num(n)
print("List of the first ",n ,"Fibnacci numbers :", lst)
List of the first  10 Fibnacci numbers : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''Q30 Check if a list is sorted.'''

def check_lst_sorted(lst) :
    for i in range(1,len(lst)) :
        if lst[i] < lst[i-1] :
            return False
    return True

lst = eval(input("Enter a list :"))
if check_lst_sorted(lst) :
    print("List is sorted in ascending order")
else :
    print("List is not sorted in ascending order")
List is sorted in ascending order
'''Q31 Rotate a list to the left by `n` positions.'''

lst = eval(input("Enter a list :"))
n = int(input("Enter number of positions to rotate list to the left :"))
rotated_lst = lst[n:] + lst[0:n]
print(f"List rotated to left by {n} positions : {rotated_lst}")
List rotated to left by 3 positions : [6, 7, 8, 9, 10, 1, 2, 11, 3, 4, 5]
'''Q32 Rotate a list to the right by `n` positions.'''

lst = eval(input("Enter a list :"))
n = int(input("Enter number of positions to rotate list to the right :"))
rotated_lst = lst[:n-1:-1] + lst[0:n]
print(f"List rotated to right by {n} positions : {rotated_lst}")
List rotated to right by 3 positions : [11, 2, 1, 10, 9, 8, 7, 6, 3, 4, 5]
'''Q33 Create a list of prime numbers up to 50.'''

#defining function prime_num()
def prime_num() :
    #crating empty list for storing prime numbers
    lst = []     
    #giving range 1 to 40 as formula to calculate prime numbers is valid till 40
    for i in range(1,41) :
        #checking for 1 and negative numbers
        if i<=1 :
            continue
        #checking for numbers 2 and 3
        elif i<=3 :
            #adding prime numbers to list
            lst.append(i)
            continue
        #checking for left numbers
        elif i in (4,51) :
            #given this range as formula is applicable on this only
            for j in range(1,10) :
                #formula 1
                p_1 = (6*j) - 1
                #formula 2
                p_2 = (6*j) + 1
                #ignoring exceptions in formula
                if p_1 not in (25,35,49,53,55) :
                    #adding prime numbers to list 
                    lst.append(p_1)
                #ignoring exceptions in formula
                if p_2 not in (25,35,49,53,55) :
                    #adding elements to list
                    lst.append(p_2)
    #returning list of prime numbers upto 50
    return lst

#initializing n = 50
n = 50
#calling funcion pime_num()
prime_num_lst = prime_num()
#printing list of prime numbers upto 50
print(f"List of prime numbers upto {n} : ")
print(prime_num_lst)  
List of prime numbers upto 50 : 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''Q34 Split a list into chunks of size `n`.'''

def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
lst = eval(input("Enter a list :"))
n = int(input("Enter size into which you want to split list :"))
chunked_list = list(chunk_list(lst, n))

print(f"List after splitting into chunks of {n} : {chunked_list}")
List after splitting into chunks of 3 : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
'''Q35 Find the second largest number in a list.'''

lst = eval(input("Enter a list :"))
max_num_1 = max(lst)
if max_num_1 in lst :
    lst.remove(max_num_1)
max_num_2 = max(lst)
print("Second largest number in list :", max_num_2)
Second largest number in list : 87
'''Q36 Replace every element in a list with its square.'''

lst = eval(input("Enter a list :"))
square_lst = list(map(lambda i : i**2 , lst))
print("Every element in list with its squares :", square_lst)
Every element in list with its squares : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''Q37 Convert a list to a dictionary where list elements become keys and their
indices become values.'''

lst = eval(input("Enter a list :"))
dictionary = dict()
for i in range(len(lst)) :
    dictionary[lst[i]] = i
print("List converted to dictionary :", dictionary)
List converted to dictionary : {'Tokyo': 0, 'Berlin': 1, 'Rio': 2, 'Paris': 3}
'''Q38 Shuffle the elements of a list randomly.'''

import random 
lst = eval(input("Enter a list :"))
random.shuffle(lst)
print("List with shuffled elements :", lst)
List with shuffled elements : ['Paris', 'Tokyo', 'Berlin', 'Rio']
'''Q39 Create a list of the first 10 factorial numbers.'''

def fact_lst(n) :
    if n == 0 :
        return 1
    else :
        return n*fact_lst(n-1)

n = int(input("Enter number of factorial numbers you want in a list (n - 1) :"))
lst = []
while n >= 0 :
    element = fact_lst(n)
    lst.append(element)
    n -= 1
lst.sort()
print(f"List of first {n} factorial numbers : {lst}")
List of first -1 factorial numbers : [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
'''Q40 Check if two lists have at least one element in common.'''

lst_1 = eval(input("Enter 1st list :"))
lst_2 = eval(input("Enter 2nd list :"))
new_lst = []
for i in lst_1 :
    for j in lst_2 :
        if i == j :
            if i in new_lst :
                continue
            else :
                new_lst.append(i)
if len(new_lst) == 0 :
    print("No element is common")
else :
    print("Two lists have atleast one element in common ")
Two lists have atleast one element in common 
'''Q41 Remove all elements from a list.'''

lst = eval(input("Enter a list :"))
length = len(lst)
for i in range(length) :
    lst.pop()
print("List after removing all the elements :", lst)
List after removing all the elements : []
'''Q42 Replace negative numbers in a list with 0.'''

lst = eval(input("Enter a list :"))
for i in range(len(lst)) :
    if lst[i] < 0 :
        lst[i] = 0
print("List after updation :", lst)
List after updation : [0, 56, 0, 0, 3, 4, 0]
'''Q43 Convert a string into a list of words.'''

string = input("Enter a string :")
lst = string.split()
print("Conversion of string into a list of words :", lst)
Conversion of string into a list of words : ['My', 'name', 'is', 'Akshat', 'Saxena', '.']
'''Q44 Convert a list of words into a string.'''

lst = eval(input("Enter a list of words :"))
string = " ".join(lst)
print("Conversion of list of words into string :",string)
Conversion of list of words into string : My name is Akshat Saxena .
'''Q45 Create a list of the first `n` powers of 2.'''

n = int(input("Enter number of powers of 2 list you want :"))
lst = []
for i in range(n) :
    lst.append(2**i)
print(f"List of first {n} powers of 2 : {lst}")
List of first 10 powers of 2 : [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
'''Q46 Find the longest string in a list of strings.'''

lst = eval(input("Enter a list of strings :"))
longest_string = max(list(map(lambda i : len(i) , lst)))
for i in lst :
    if len(i) == longest_string :
        print("Longest string in list of strings :", i)
Longest string in list of strings : Berlin
'''Q47 Find the shortest string in a list of strings.'''

lst = eval(input("Enter a list of strings :"))
shortest_string = min(list(map(lambda i : len(i) , lst)))
for i in lst :
    if len(i) == shortest_string :
        print("Shortest string in list of strings :", i)
Shortest string in list of strings : Rio
'''Q48 Create a list of the first `n` triangular numbers.'''

def triangular_numbers(n) :
    return [i * (i+1) // 2 for i in range(1,n+1)]

n = int(input("Enter number of first n triangular numbers you want :"))
lst = triangular_numbers(n)
print(f"List of the first {n} triangular numbers : {lst}")
List of the first 10 triangular numbers : [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
'''Q49 Check if a list contains another list as a subsequence.'''

def check_subsequence(lst , subsequence) :
    index = 0
    for i in lst :
        if i == subsequence[index] :
            index += 1
            if index == len(subsequence) :
                return True
    return False
            

lst = eval(input("Enter a list :"))              
subsequence = eval(input("Enter another list :")) 

result = check_subsequence(lst,subsequence)
if result :
    print("List ccontains another list as subsequence")
else :
    print("List does not contain another list as subsequence")
List ccontains another list as subsequence
'''Q50 Swap two elements in a list by their indices.'''

lst = eval(input("Enter a list :"))
ele_1 = int(input("Enter element 1 to swap :"))
ele_2 = int(input("Enter element 2 to swap :"))
if ele_1 in lst and ele_2 in lst :
    index_1 = lst.index(ele_1)
    index_2 = lst.index(ele_2)
lst[index_1] = ele_2
lst[index_2] = ele_1
print("List after updation :", lst)
List after updation : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
