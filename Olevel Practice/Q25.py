# Wap to check whether a no. is prime or not.

N = int(input("Enter no"))
count = 0
i = 1
if N <= 1:
    print(f"{N} is not a prime no.")
else:
    while i <= N:
        if N % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(f"{N} is a prime no.")
    else:
        print(f"{N} is not a prime no.")
