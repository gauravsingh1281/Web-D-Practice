# Encode the string into ASCII code
input_string = input("Enter string: ")
encoded_string = ""
for char in input_string:
    ascii_code = ord(char)
    encoded_string += str(ascii_code)
print(encoded_string)
