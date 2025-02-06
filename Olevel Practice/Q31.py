# WAP to count the total number of even and odd numbers in the list.
list = []
evenCount = 0
oddCount = 0
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
for j in list:
    if j % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(
    f"Total number of even numbers = {evenCount} and odd numbers = {oddCount} in the list {list}"
)
