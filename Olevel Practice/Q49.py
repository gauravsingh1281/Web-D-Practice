# 1 Wap to display months and days for entered no. of days
days = int(input("enter days"))
month = days / 30
days = days % 30
print(f"{int(month)} Months {days} days")

# 2 Wap to swap two variables values
x = int(input("Enter x"))
y = int(input("Enter y"))
print(f"Value of x {x} and y {y} before swaping")
temp = x
x = y
y = temp
print(f"Value of x {x} and y {y} after swaping")

# 3 Wap to swap two variables values without using temporary variables.
x = int(input("Enter x"))
y = int(input("Enter y"))
print(f"Value of x {x} and y {y} before swaping")
x, y = y, x
print(f"Value of x {x} and y {y} after swaping")

# 4 Wap to generate a random no.
import random

randomNo = random.randint(0, 9)
print(randomNo)

# 5 WAP to find the greatest number between three numbers
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if a > b and a > c:
    print("a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")
# 6 WAP to find the greatest number between 4 numbers
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
d = int(input("Enter the 4th number: "))

if a > b and a > c and a > d:
    print("a is greater")
elif b > c and b > d:
    print("b is greater")
elif c > d:
    print("c is greater")
else:
    print("d is greater")

# 7 Wap to find the largest no. betm two ternary operator
a = 45
b = 4
print("a is greater") if a > b else print("b is greater")

# 8 Wap to check a year is leap year or not
year = int(input("Enter year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
