# range(): values between the range

# print(range(10))
# print(list(range(10)))
# print(list(range(5, 11)))
# # # print only odd numbers
# print(list(range(1, 10, 2)))
# # # print only even numbers
# # print(list(range(2, 10, 2)))
# #
# print(list(range(10, 1, -1)))
#
# print(list(range(10, 3)))

# while loop

# initialization
# condition
# incrementation
# i = 1
# while i < 10:
#     print(i)
#     i += 1
# print("Done!!!")

# for loop

# for i in range(10):
#     print(i)
# ascending / descending / multiple

# jumping statements
# break and continue

# for i in range(1, 10):
#     if i == 3:
#         continue
#     print(i)
#
# print("program exited")

# Numbers and Strings

# num1 = 100
# num2 = 13.2
#
# print(type(num1))
# print(type(num2))

# find maximum and minimum of 3 numbers max() & min()
# print(max(23, 21, 43, 22, 66))
# print(min(23, 21, 43, 22, 66))

# print(max(23.3, 21, 43, 22, 66.4))
# print(min(23, 21, 43, 22, 66))

# ways of creating string variables
# s = 'welcome'
# s = "welcome Back"
# s = str('43')
# s = str("43")

# mutable - can change the value of the variable
# immutable - cannot change the value of the variable
# string is immutable

# str1 = "welcome"
# print(id(str1))

# str1 = str1 + " to python"
# print(id(str1))

# i = 43
# print(id(i))
# i = 432
# print(id(i))

# concatenation with + and *
# s = "Welcome" + " to Python"
# print(s)
# print(s * 3)


# slicing operators
# str1 = "welcome"
# print(str1[1:3])
# print(str1[:3])
# print(str1[3:])

# ord() and chr()

# ord() gives ASCII number of character
# print(ord('f'))
# print(ord('F'))

# chr() gives character of given ASCII number
# print(chr(200))

# max(), min(), len()
# print(max("ABCeDF"))
# print(min("abcde"))
# print(len("abcde"))

# in, not in operators
# s = "welcome"
# print("come" in s)
# print("lome" in s)
#
# print("come"  not in s)
# print("lome" in s)

# String comparison
# print("tim" == "tie")
# print("free" != "freedom")
# print("arrow" > "ARROW")
# print("right" >= "left")
# print("teeth" <= "tee")
# print("yellow" <= "fellow")
# print("abc" > "")

# testing strings: True/False
s = "welcome to python"
print(s.isalnum())
print(s.isalpha())
print("2021".isdigit())
print("count".isidentifier())
print(s.islower())
print("WELCOME".isupper())
print(" ".isspace())

# Searching for substrings
s = "welcome to python"
print(s.endswith("thon"))
print(s.startswith("good"))
print(s.find("come"))
print(s.find("become"))
print(s.count("o"))
print(f"{s[:4]}")

# converting string
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)
#
# s2 = s.title()
# print(s2)
#
# s3 = s.lower()
# print(s3)
#
# s4 = s.upper()
# print(s4)
#
# s5 = s.swapcase()
# print(s5)

# s6 = s.replace("in", "on")
# print(s6)

# reverse a string
# s = "welcome"
# rev_str = ""
# for i in s:
#     rev_str = i + rev_str
    # print(rev_str)
# print(rev_str)

# next way
# rev_str = s[::-1]
# print(rev_str)
