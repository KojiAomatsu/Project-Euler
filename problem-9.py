def find(n):
    for i in range(1, n//3):
        for j in range(i, n-i//2):
            if i**2 + j**2 == (1000-i-j)**2:
                return i*j*(1000-i-j)

print(find(1000))
