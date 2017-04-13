def calc():
    result = 0
    for i in range(2, 1000000):
        summa = 0
        for j in str(i):
            summa += int(j)**5
        if i == summa:
            result += i
    
    return result

print(calc())
