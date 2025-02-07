# WAP to find the Maximum and Second maximum value in the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
if listSize < 2:
    print("The list should contain at least 2 elements")
else:
    list.sort(reverse=True)
    maxValue = list[0]
    secondMaxValue = list[1]
    print(f"Maximum value in the list {list} = {maxValue}")
    print(f"Second Maximum value in the list {list} = {secondMaxValue}")
