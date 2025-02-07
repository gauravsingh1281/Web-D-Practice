# WAP to find the Minimum and Second minimum value in the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)

if listSize < 2:
    print("The list must contain at least two elements.")
else:
    list.sort()
    minValue = list[0]
    secondMinValue = list[1]
    print(f"Minimum value in the list {list} = {minValue}")
    print(f"Second Minimum value in the list {list} = {secondMinValue}")
