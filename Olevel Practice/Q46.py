# WAP to find the palindrome in given range 200 to 500


def palindromeCheck(N):
    originalNo = N
    reverseNo = 0
    while N > 0:
        reverseNo = reverseNo * 10 + N % 10
        N //= 10
    if originalNo == reverseNo:
        print(f"{originalNo} is a palindrome")


for i in range(200, 501):
    palindromeCheck(i)
