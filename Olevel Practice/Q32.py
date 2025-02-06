# WAP to find the sum of even numbers and product of odd numbers in the list.
list = []
evenSum = 0
oddProduct = 1
listSize = int(input("How many elements do you want in the list? "))
for i in range(listSize):
    listElement = int(input("Enter value: "))
    list.append(listElement)
for j in list:
    if j % 2 == 0:
        evenSum += j
    else:
        oddProduct *= j
print(
    f"Sum of even numbers = {evenSum} and product of odd numbers = {oddProduct} in the list {list}"
)
