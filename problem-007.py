def prime_maker(num):
    primes = [2]
    for i in range(3, num+1):
        flag = True
        for n in primes:
            if i < n**2:
                break
            elif i%n == 0:
                flag = False
        if flag == True:
            primes.append(i)
    return primes

primes = prime_maker(150000)
print(primes[10000])
