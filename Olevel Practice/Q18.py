# Wap to print the sum of the sqaure of digits of a given no.
N = input("Enter a number to find the sum of the square of its digits: ")
num = int(N)
sum = 0

while num > 0:
    digitSquare = (num % 10) ** 2
    sum += digitSquare
    num //= 10

print(f"Sum of sqaure of digit of {N} = {sum}")
