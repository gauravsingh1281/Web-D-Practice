# WAP to check if a number is a palindrome or not.
originalNo = int(input("Enter a number: "))
num = originalNo
reverseNo = 0

while num > 0:
    reverseNo = (reverseNo * 10) + (num % 10)
    num //= 10

if reverseNo == originalNo:
    print(f"{originalNo} is a palindrome")
else:
    print(f"{originalNo} is not a palindrome")
