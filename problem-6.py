def calc(n):
    square = 0
    the_sum = 0
    for i in range(1, n+1):
        square += i
        the_sum += i**2
    return square**2 - the_sum

print(calc(100))
