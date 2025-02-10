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
