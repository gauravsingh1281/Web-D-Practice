# 1 Encode the string into ASCII code
input_string = input("Enter string: ")
encoded_string = ""
for char in input_string:
    ascii_code = ord(char)
    encoded_string += str(ascii_code)
print(encoded_string)

# 2 Wap to find the factors of a no.
N = int(input("enter no."))
i = 1
while i <= N:
    if N % i == 0:
        print(i)
    i += 1

# 3 Wap to find the sum of factors of a no.
N = int(input("enter no."))
i = 1
factorSum = 0
while i <= N:
    if N % i == 0:
        factorSum += i
    i += 1
print(f"Sum of factors of {N} = {factorSum}")


# 4 Fibonacci Series
n = int(input("enter no."))
series = []
if n == 1:
    series = [0]
elif n == 2:
    series = [0, 1]
else:
    series = [0, 1]
    for i in range(2, n + 1):
        series.append(series[-2] + series[-1])
for j in series:
    print(j)
