n = float(input())
x = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

def mean():
    divisor = sum(w)
    zipped = zip(x, w)
    dividend = 0

    for t in zipped:
        dividend += t[0] * t[1]

    print round(dividend / divisor, 1)

mean()