import math

n = float(input())
numbers = sorted([int(i) for i in raw_input().split()])

def median(arr):
    k = len(arr)
    even = k % 2 == 0
    if even:
        snd = int(k / 2)
        fst = snd - 1
        return (arr[fst] + arr[snd]) / 2
    else:
        return arr[int(math.ceil(k / 2))]

Q2 = median(numbers)

Q1 = median([x for x in numbers if x < Q2])
Q3 = median([x for x in numbers if x > Q2])

print(Q1)
print(Q2)
print(Q3)