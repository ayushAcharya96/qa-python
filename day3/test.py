# def changeCharacterInString(inputString):
#     temp_char = ""
#     result_string = ""
#     for i in inputString:
#         if temp_char == "":
#             temp_char = i
#             result_string += i
#         elif temp_char == i:
#             result_string += "$"
#         else:
#             result_string += i
#     return result_string
# result = changeCharacterInString("airplane")
# print(result)
# print(changeCharacterInString("example"))
#
# None
# def functionName(arg1, arg2):
#     # function body
#     print("Result")
#     return 0
#
# def swichCharacter(givenString):
#     return givenString[-1] + givenString[1:-1] + givenString[0]
#
# print(swichCharacter("apple"))

# Collection
# list
# tuple
# dictionary
# set

# list
# collection of data
# ordered,
# indexed
# mutable

# fruits = []
# fruits = ["apple", "banana", "cherry"]
# fruits.append("dragon fruit")
# print(fruits)
# fruits.pop()
# fruits[1] = "orange"
# print(fruits)
# del fruits[1]
# print(fruits)
# print(fruits[0])
#
# print(len(fruits))

# fruits = ["apple", "banana", "cherry"]
# num = [1,2,3,4,3,4,5]
# fruits.insert(2,"mango")
# print(fruits)
#

# print(num.count(3))
# print(id(num))
# num2 = num.copy()
# print(id(num2))
# num3 = num
# print(id(num3))
# print(num)
# num.append(4)
# print(num3)

# fruits = fruits + num
# print(fruits)
# for i in fruits:
#     print(i)



## Tuple
# indexed
# ordered
# immutable

# t = ("apple", "banana", "cherry")
# print(t.index("cherry"))
# for i in t:
#     print(i)
# print(t)
# a = list(t)
# print(a)
# a.append("mango")
# t = tuple(a)
# print(t)

# Set
# unordered
# unindexed
# mutable

# s1 = {"apple", "banana", "cherry", 1, 2, 3}
# s2 = {1,2,3}
# # print(s)
# # print(s)
# # print(s1.intersection(s2))
# s1.add(5)
# print(s1)
# s1.update({"abc", "xyz"})
# print(s1)


# Dictionary
# key value pair
# unordered
# unindexed
# mutable

dict = {
    "apple": 100,
    "banana": 200,
    "cherry": 300
}
# print(dict.get("apple"))
# print(dict["banana"])
for key, value in dict.items():
    print(key, value)

list = [1,2,3]
list.extend([3,4])
print(list)













