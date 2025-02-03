# Wap to print the sum of the digits of a given no.
N = input("Enter no. to find the sum of its digits")
sum = 0
for digit in N:
    sum = sum + int(digit)
print(f"Sum of digit of {N} = {sum}")
