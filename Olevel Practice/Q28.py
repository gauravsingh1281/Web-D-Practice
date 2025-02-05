# WAP to capitalize the first and last letter of each word in a given string.
str = input("Enter string: ")
words = str.split()
newstring = ""

for word in words:
    if len(word) > 1:
        newstring += word[0].upper() + word[1:-1] + word[-1].upper() + " "
    else:
        newstring += word.upper() + " "

print(newstring.strip())
