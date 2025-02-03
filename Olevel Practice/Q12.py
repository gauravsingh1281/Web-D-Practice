# Wap to find the factorial of N no.
N = int(input("Enter any no. know its factorial"))
fact = 1
# using while loop
i = 1
while i <= N:
    fact = fact * i
    i += 1

# using for loop
for j in range(1, N + 1):
    fact = fact * j
print(f"Factorial of {N} = {fact}")
