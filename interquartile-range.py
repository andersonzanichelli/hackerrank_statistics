import math

n = float(input())
elements = [int(i) for i in raw_input().split()]
frequency = [int(i) for i in raw_input().split()]

def median(arr):
    k = len(arr)
    even = k % 2 == 0
    if even:
        snd = int(k / 2)
        fst = snd - 1
        return ((arr[fst] + arr[snd]) / 2, (fst + snd) / 2)
    else:
        return (arr[int(math.ceil(k / 2))], int(math.ceil(k / 2)))

def create_dataset(zipped):
    numbers = []
    for x in zipped:
        k = 0
        while k < x[1]:
            numbers.append(x[0])
            k += 1
    return sorted(numbers)

zipped = zip(elements, frequency)
numbers = create_dataset(zipped)

idxQ2 = median(numbers)

Q1 = median([x for i,x in enumerate(numbers) if i <= idxQ2[1]])
Q3 = median([x for i,x in enumerate(numbers) if i > idxQ2[1]])

print math.floor(Q3[0] - Q1[0])