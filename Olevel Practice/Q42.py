# WAP to create a dictionary with the roll no., name, and marks of N students in a class and display the name of students who have marks more than 75.

N = int(input("Enter number of students: "))
record = {}
for i in range(N):
    r = int(input("Roll No.: "))
    n = input("Name: ")
    m = float(input("Marks: "))
    record[r] = [n, m]

for key in record:
    if record[key][1] > 75:
        print(record[key][0])
