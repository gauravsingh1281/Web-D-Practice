# WAP to reverse the list
list = []
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
listReverse = []
for j in range(listSize - 1, -1, -1):
    listReverse.append(list[j])

print(f"Reverse of the list {list} = {listReverse}")
