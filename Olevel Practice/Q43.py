# WAP to create a dictionary with the roll no. and percentage of 10 students in a class and display the roll no of students who have percentage more than 50.

record = {}
studentSize = 10

for i in range(studentSize):
    rollNo = int(input("Enter roll no: "))
    percentage = float(input("Enter percentage: "))
    record[rollNo] = percentage

for j in record:
    if record[j] > 50:
        print(j)
