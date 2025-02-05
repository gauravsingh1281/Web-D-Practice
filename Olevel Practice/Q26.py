# WAP to count the number of times a character occurs in the given string.
str = input("Enter string: ")
charToCheck = input("Enter character to find its occurrence: ")
count = 0

for char in str:
    if char == charToCheck:
        count += 1

print(f"'{charToCheck}' occurs {count} times in '{str}'")
