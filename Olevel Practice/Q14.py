# Wap to generate fibonacci series up to N terms entered by the user.
N = int(input("Ente no. of term upto which you want to generate fibonacci series"))


def fibonacciGenerator(N):
    series = []
    if N == 1:
        series = [0]
    elif N == 2:
        series = [0, 1]
    else:
        series = [0, 1]
        for i in range(2, N):
            series.append(series[-2] + series[-1])
    return series


print(fibonacciGenerator(N))
