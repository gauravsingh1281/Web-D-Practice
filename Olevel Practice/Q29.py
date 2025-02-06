# Wap to count the total no. of vowel and consonants in the given string.
str = input("Enter string: ").lower()
vowelCount = 0
consonentCount = 0
vowels = "aeiou"
# 1st method

# for i in range(0, len(str)):
#     if str[i] != "":
#         if (
#             str[i] == "a"
#             or str[i] == "i"
#             or str[i] == "e"
#             or str[i] == "o"
#             or str[i] == "u"
#         ):
#             vowelCount += 1
#         else:
#             consonentCount += 1

# 2nd method
for char in str:
    if char.isalpha():
        if char in vowels:
            vowelCount += 1
        else:
            consonentCount += 1

print(f"Total no. of vowel in given string '{str}' = {vowelCount}")
print(f"Total no. of consonent in given string '{str}' = {consonentCount}")
