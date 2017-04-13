def calc():
    result = 1
    for i in range(1, 501):
        result += (i*2+1)**2 * 4 - 2*i - 4*i - 6*i
    return result

print(calc())
