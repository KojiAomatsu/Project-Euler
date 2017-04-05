from eulerlib import primes

def calc(n):
    prime_list = primes(n)
    result = 0
    for num in prime_list:
        result += num
    return result

print(calc(2000000))
