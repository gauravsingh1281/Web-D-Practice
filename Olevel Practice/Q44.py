# WAP to find the factorial of a number using recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter number to find its factorial: "))
if num < 0:
    print(f"Factorial is not defined for the negative number {num}")
else:
    print(f"Factorial of {num} = {fact(num)}")
