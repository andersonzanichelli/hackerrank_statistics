import math

n = float(input())
numbers = sorted([int(i) for i in raw_input().split()])

def mean():
    return round((sum(numbers)/n), 1)

def standard_deviation():
    m = mean()
    s = 0
    for x in numbers:
        s += (x - m) ** 2.0

    print round(math.sqrt(s / n), 1)

standard_deviation()