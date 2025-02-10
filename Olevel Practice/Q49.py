# 1 Wap to display months and days for entered no. of days
days = int(input("enter days"))
month = days / 30
days = days % 30
print(f"{int(month)} Months {days} days")
