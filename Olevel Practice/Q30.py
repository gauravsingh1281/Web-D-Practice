# WAP to find the sum of the elements of a list

# For predefined list elements

# list1 = [23, 45, 34, 67, 433, 64]
# sum1 = 0
# for element in list1:
#     sum1 += element
# print(f"Sum of elements of the list {list1} = {sum1}")

# For dynamic list elements
list2 = []
sum2 = 0
N = int(input("How many elements do you want in the list? "))
for i in range(N):
    listElement = int(input("Enter value: "))
    list2.append(listElement)

for element in list2:
    sum2 += element
print(f"Sum of elements of the list {list2} = {sum2}")
