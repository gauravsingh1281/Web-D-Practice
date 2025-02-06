# WAP to find the frequency of the element in the list
list = []
count = 0
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
elementCount = int(input("Enter element to count in the list: "))
for j in list:
    if elementCount == j:
        count += 1
print(f"Frequency of the element {elementCount} in the list {list} = {count}")
