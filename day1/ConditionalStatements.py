# Example 1 print a person is eligible for vote or not

age = 15

if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Example 2

if True:
    print("True Condition")
else:
    print("False condition")

# Example 3:

if 1:
    print("One")
else:
    print("not one")

# Example 4:
# Find a number is even/odd
num = 10

if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")

# Example 5: if else in single line (ternary operator)
num = 11
print("Even number") if num % 2 == 0 else print("Odd number")

# Example 6: if else - multiple statements in single line
a = 20
{print("hello"), print("python")} if a > 10 else {print("hello"), print("java")}

# Example 7: Multiple conditions using elif
day = 1
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    pring("Invalid day")
