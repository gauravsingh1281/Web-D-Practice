# WAP to find the product of the digits of a given number

N = int(input("Enter a number to find the product of its digits: "))
originalN = N
product = 1

while N > 0:
    product *= N % 10
    N //= 10

print(f"Product of the digits of {originalN} = {product}")
