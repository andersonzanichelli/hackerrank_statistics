import math
import operator

n = float(input())
numbers = sorted([int(i) for i in raw_input().split()])

def mean():
    print round((sum(numbers)/n), 1)

def median():
    even = n % 2 == 0
    if even:
        snd = int(n / 2)
        fst = snd - 1
        print round(((numbers[fst] + numbers[snd]) / 2.0), 1)
    else:
        print round(numbers[int(math.ceil(n / 2))], 1)

def mode():
    dic = {}
    for i in numbers:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    dic_order = sorted(dic.items(), key=operator.itemgetter(1))
    if max(dic_order) == 1:
        mode = numbers[0]
        print mode
    else:
        m = max(dic, key=dic.get)
        result = [i for i in dic_order if i[1] == dic[m]]
        t = min(result)
        print t[0]

mean()
median()
mode()