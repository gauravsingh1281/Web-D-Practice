# WAP to find the maximum number of the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
maxValue = list[0]
for j in range(listSize):
    if maxValue < list[j]:
        maxValue = list[j]
print(f"Maximum number in the list {list} = {maxValue}")
