#1.Write a Python program to calculate the length of a string.
Text = "Shoppe"
print(len(Text))

#2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def counttheumberofcharacters(a):
    Text1 = {}
    for char in a: #Duyệt từng ký tự trong chuỗi
        if char in Text1: 
            Text1[char] += 1 #Nếu ký tự có trong thư viện thì tăng thêm 1
        else:
            Text1[char] = 1  #Nếu ký tự không có trong thư viện thì = 1
    return Text1

Text2 = "google.com"
print(counttheumberofcharacters(Text2))

#3. Write a  Python program to get a string made of the first 2 and last 2 characters of a given 
#string. If the string length is less than 2, return the empty string instead. 

Text3 = "w3resource"
if len(Text3) < 2:
    print("Empty String")
else:
    print(f"{Text3[:2]+Text3[-2:]}")

#4. Write a  Python program to get a string from a given string where all occurrences of its first 
#char have been changed to '$', except the first char itself. 
Text4 = "restart"
print(Text4[0] + Text4[1:].replace(f"{Text4[0]}","$"))

#5. Write a  Python program to get a single string from two given strings, separated by a space and 
#swap the first two characters of each string. 
Text5 = "abc"
Text6 = "xyz"
Text7 = Text6.replace(f"{Text6[-1:]}","") + Text5[-1:]
Text8 = Text5.replace(f"{Text5[-1:]}","") + Text6[-1:]
print(f"{Text7} {Text8}")

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If 
#the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is 
#less than 3, leave it unchanged. 
def addingorly(a):
    if len(a) >=3 and a[-3:] == "ing":
        a1 = a + "ly"
    elif len(a) >=3:
        a1 = a + "ing"
    else:
        a1 = "unchanged"
    return a1

Text9 = addingorly("abcing")
print(Text9)

# 7. Write a  Python program to find the first appearance of the substrings 'not' and 'poor' in a given 
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the 
# resulting string. 
Text10 = "The lyrics is not that poor!"
Text11 = Text10.find("not")
Text12 = Text10.find("poor")
if Text11 < Text12:
    Text13 = Text10[:Text11] + "good" + Text10[Text12 + 4:]
    print(Text13)


# 8. Write a Python function that takes a list of words and return the longest word and the length
# of the longest one.
Fruit = ['Bananas','Apple','Orange','Strawbery']
longest_word = ""
max_length = 0

for i in Fruit:
    if len(i) > max_length:
        longest_word = i 
        max_length = len(i)
print(longest_word,max_length)

# 9. Write a Python program to remove the nth index character from a nonempty string.
def remove(Text13,n):
    if n < 0 or n >= len(Text13):
        return "n khong hop le"
    else:
        return Text13[:n] + Text13[n+1:] # Text13[n+1:] Khi n == len(s) - 1 slice sẽ nhận diện là chuỗi rỗng nếu là ký tự cuối

Text13 = input("Input your string")
n = int(input("Nhập vị trí cần xóa"))
print(remove(Text13,n))

# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged."
Text14 = "Special"
Text17 = Text14[-1:] + Text14[1:-1] + Text14[:1] 
print(Text17)


# 11. Write a Python program to remove characters that have odd index values in a given string. 
Text18 = "Orange"
Text19 = ""
for char in Text18:
    a = Text18.find(char)
    if a % 2 == 0:
        Text19 += char
print(Text19)

#12. Write a Python program to count the occurrences of each word in a given sentence.
# Giong voi bai 2 

# 13. Write a  Python  script that takes input from the user and displays that input back in upper 
# and lower cases.
Text20 = input("Enter your string")
print(Text20.upper())
print(Text20.lower())

# 14. Write a Python program that accepts a comma-separated sequence of words as input and 
# prints the distinct words in sorted form (alphanumerically).
Text21 = "red, white, black, red, green, black"
Text22 = Text21.split(",")
Text23 = []
for word in Text22:
    Text23.append(word.strip())
Text24 = sorted(set(Text23))
result = ", ".join(Text24)
print(result)

# 15. Write a  Python function to create an HTML string with tags around the word(s)
def tags(a,b):
    return f"<{a}>{b}</{a}>"
print(tags("i","Python"))

# 16. Write a Python function to insert a string in the middle of a string.
def tagss(a,b):
    mid = len(a) // 2 #dùng // thay vì / để đảm bảo mid là số nguyên
    return a[:mid] + b +a[mid:]

print(tagss("{{}}","PHP"))

# 17. Write a Python function to get a string made of 4 copies of the last two characters of a 
# specified string (length must be at least 2).
def insert_end(a):
    a1 = a[-2:] * 4
    return a1
Text24 = "Python"
print(insert_end(Text24))

# 18. Write a  Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string. 
# Sample function and result : 
def first_three(a):
    if len(a) < 3:
        return a
    else:
        a1 = a[:3]
        return a1

print(first_three(Text24))


# 19. Write a Python program to get the last part of a string before a specified character.
def get_the_last_part_of_a_string(a,b):
    a1 = a.rfind(b)
    a2 = a[:a1]
    return a2

Text25 = input("Enter your string")
Text26 = input("Enter your specified character")
print(get_the_last_part_of_a_string(Text25,Text26))

# 20. Write a  Python function to reverse a string if its length is a multiple of 4. 
def reverse_a_string(a):
    if len(a) % 4 == 0:
        a1 = a[::-1]
        return a1
    else:
        return "độ dài của chuỗi không phải là bội số của 4"
    
Text27 = "Orangeee"
print(reverse_a_string(Text27))

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 
# uppercase characters in the first 4 characters.
def all_uppercase(a):
    a1 = a[:4]
    count = 0
    for char in a1:
        if char.isupper() == True:
            count += 1
    if count >= 2:
        a2 = a.upper()
    return a2

Text28 = "OOganee"
print(all_uppercase(Text28))
        
# 22.Write a  Python program to sort a string lexicographically.
Text29 = "Hello"
Text30 = "".join(sorted(Text29))
print(Text30)

# 23. Write a Python program to remove a newline in Python.
Text31 = "Xinchao\nmoinguoi"
print(Text31.replace("\n",""))

# 24. Write a Python program to check whether a string starts with specified characters. 
def check(a,b):
    if a.startswith(b):
        return f"chuỗi của bạn bắt đầu ký tự {b}"
    else:
        return f"chuỗi của bạn không bắt đầu ký tự {b}"

Text32 = "Whatthehell"
Text33 = "W"
print(check(Text32,Text33))

# 25. Write a Python program to create a Caesar encryption.
def Caesar_encryption(a,b):
    Text23 = ""
    for char in a:
        if char.isupper(): #kiểm tra chữ in hoa
            Text23 += chr((ord(char)-ord("A") + b) % 26 + ord("A"))
        elif char.islower():
            Text23 += chr((ord(char)-ord("a") + b) % 26 + ord("a"))
        else:
            Text23 += char
    return Text23

input_text = input("Nhập văn bản cần mã hóa:")
shift_value = int(input("Nhập số bước dịch chuyển: "))
print(f"Văn bản mã hóa là{Caesar_encryption(input_text,shift_value)}")

# 26. Write a  Python program to display formatted text (width=50) as output.
Text24 = "Hello, Word!" 
print(f"{Text24:<50}")

# 27. Write a  Python program to remove existing indentation from all of the lines in a given text. 
def remove_existing_indentation(a):
    a1 = a.split("\n")
    a2 = []
    for string in a1:
        a2.append(string.lstrip())
    return "\n".join(a2)

Text25 = """
This is a test.
    Another line with indentation.
        This line has more indentation.
    Final line. """

print(remove_existing_indentation(Text25))