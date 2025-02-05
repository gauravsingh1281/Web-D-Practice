# WAP to check if a string is palindrome or not

# 1st method
str = input("Enter string: ")
reverseString = str[::-1]
if str == reverseString:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")

# 2nd method
reverseString2 = ""
for i in range(len(str) - 1, -1, -1):
    reverseString2 += str[i]
if str == reverseString2:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")
