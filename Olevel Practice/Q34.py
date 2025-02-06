# WAP to search for all occurrences of the number in the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
searchElement = int(input("Enter value to search in the list: "))

indices = []
for j in range(listSize):
    if list[j] == searchElement:
        indices.append(j)

if indices:
    print(f"Element {searchElement} found at indices {indices} of the list {list}")
else:
    print(f"Element {searchElement} not found in the list {list}")
