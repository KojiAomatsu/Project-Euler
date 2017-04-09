import sympy

def abundant(n):
    summa = 1
    factors = sympy.factorint(n)
    for i in factors.keys():
        num = 0
        index = factors[i]
        for j in range(index + 1):
            num += i**j
        summa *= num
    if summa > n * 2:
        return True
    else:
        return False

def calc():
    result = 0
    for i in range(1, 28514):
        flag = False
        for j in range(12, i//2 + 1):
            k = i - j
            if abundant(j) and abundant(k):
                flag = True
        if flag == False:
            result += i
    return result

print(calc())
