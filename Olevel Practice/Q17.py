# Wap to print the sum of the digits of a given no.
N = input("Enter no. to find the sum of its digits")
sum = 0
digit = int(N)

# 1st way
# for digit in N:
#     sum = sum + int(digit)
# print(f"Sum of digit of {N} = {sum}")

# 2nd way

while digit > 0:
    sum = sum + digit % 10
    digit = digit // 10
print(f"Sum of digit of {N} = {sum}")
