def calc(n):
    result = 1
    maxi = 1
    for i in range(1,n):
        num = i
        length = 1
        while num != 1:
            if num%2 == 0:
                num = num/2
            else:
                num = 3 * num +1
            length += 1
        if length > maxi:
            maxi = length
            result = i
    return result

print(calc(1000000))
