# pattern printing 1
N = int(input("Enter no. of row"))
i = 1
while i <= N:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

# in reverse
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print("*", end="")
        j -= 1
    print()
    i += 1
