# WAP to search for the first occurrence of the number in the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
searchElement = int(input("Enter value to search in the list: "))
found = False
for j in range(listSize):
    if list[j] == searchElement:
        print(f"Element {searchElement} found at index {j} of the list {list}")
        found = True
        break

if found == False:
    print(f"Element {searchElement} not found in the list {list}")
