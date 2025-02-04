# WAP to check if a number is Armstrong or not
originalNum = input("Enter a number to check if it is Armstrong or not: ")
num = int(originalNum)
sumOfDigit = 0

while num > 0:
    digit = num % 10
    powerOfDigit = digit ** len(originalNum)
    sumOfDigit += powerOfDigit
    num //= 10

if int(originalNum) == sumOfDigit:
    print(f"{originalNum} is an Armstrong number.")
else:
    print(f"{originalNum} is not an Armstrong number.")
