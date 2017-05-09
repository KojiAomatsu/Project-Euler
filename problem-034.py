def factorial(n):
    if n == 0:
        return 1
    elif n <= 1:
        return n
    else:
        return n * factorial(n-1)

def calc():
    result = []
    for i in range(10, 30000000):
        summa = 0
        for j in str(i):
            summa += factorial(int(j))
        if i == summa:
            result.append(i)
    return sum(result)

print(calc())
