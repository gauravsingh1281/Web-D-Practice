# WAP to find the reverse of a given number.
originalNo = int(input("Enter a number: "))
num = originalNo
reverseNo = 0

while num > 0:
    reverseNo = (reverseNo * 10) + (num % 10)
    num //= 10

print(f"Reverse of {originalNo} = {reverseNo}")
