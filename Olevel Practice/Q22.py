# WAP to find the number of even and odd digits of a given number.
originalN = int(input("Enter a number: "))
num = originalN
evenCount = 0
oddCount = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    num //= 10

print(
    f"Number of even digits = {evenCount} and number of odd digits = {oddCount} of the number {originalN}"
)
