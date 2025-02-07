# WAP to find the minimum number of the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
minValue = list[0]
for j in range(listSize):
    if minValue > list[j]:
        minValue = list[j]
print(f"Minimum number in the list {list} = {minValue}")
