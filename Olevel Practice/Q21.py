# WAP to find the sum of even and product of odd digits of a given number.
originalN = int(input("Enter a number: "))
N = originalN
evenSum = 0
oddProduct = 1

while N > 0:
    digit = N % 10
    if digit % 2 == 0:
        evenSum += digit
    else:
        oddProduct *= digit
    N //= 10

print(
    f"Sum of even digits = {evenSum} and product of odd digits = {oddProduct} of the number {originalN}"
)
