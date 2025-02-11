# Wap to remove a given from the list.
list = []
listSize = int(input("enter size"))
for i in range(listSize):
    listElement = int(input("element value"))
    list.append(listElement)
removeEl = int(input("Element to remove"))  # Convert to integer
if removeEl in list:
    list.remove(removeEl)
else:
    print("the element you want to remove does not exist in the list")

print(list)
