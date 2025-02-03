# wap to find the sum of first N even no.
N = int(input("Enter no. how many even no. you want to add."))
i = 1
sum = 0
count = 0
while count < N:
    if i % 2 == 0:
        sum += i
        count += 1
    i += 1

print(f"Sum of first {N} even no. = {sum} ")
