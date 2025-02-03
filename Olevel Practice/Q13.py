# Wap to find the year is leap year or not

year = int(input("Enter year"))


def checkLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap Year")
    else:
        print(f"{year} is not a leap Year")


checkLeapYear(year)
