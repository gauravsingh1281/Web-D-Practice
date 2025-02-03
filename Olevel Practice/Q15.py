# Wap to print the sum of no which is divisible by 7 from 1 to 500
i = 1
sum = 0
while i <= 500:
    if i % 7 == 0:
        sum += i
    i += 1
print(f"Sum of no. which is divisible by 7 between 1 to 500 = {sum}")
