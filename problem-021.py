from eulerlib import Divisors

def sum_divis(n, div):
    summa = 0
    for ele in div.divisors(n):
        summa += ele
    summa -= n
    return summa

def calc(n):
    ammic = []
    mydiv = Divisors(n)
    for i in range(2, n):
        j = sum_divis(i, mydiv)
        if sum_divis(j, mydiv) == i and i != j:
            ammic.append(i)
    result = 0
    for ele in ammic:
        if ele < n:
            result += ele
    return result

print(calc(10000))
