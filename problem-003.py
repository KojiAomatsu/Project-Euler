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

def factorization(num, primes, perfect_factorization = True):
    factors = []
    number = num
    if perfect_factorization:
        if num > primes[-1]**2:
            return ['Error. Not much primes.']
        while number != 1:
            for i in primes:
                if number%i == 0:
                    factors.append(i)
                    number = number/i
        return factors
    else:
        factors.append(number)
        for i in primes:
            if number%i == 0:
                factors.pop()
                factors.append(i)
                factors.append(number/i)
                break
        return factors

answer1 = factorization(600851475143, prime_maker(10000), False)
print(answer1) #[71, 8462696833.0]
answer2 = factorization(answer1[-1], prime_maker(10000), False)
print(answer2) #[839, 10086647.0]
answer3 = factorization(answer2[-1], prime_maker(10000))
print(answer3[-1]) #6857
