from eulerlib import Divisors

def calc():
    mydiv = Divisors(100000000)
    searching = True
    number = 3
    t = 2
    while searching:
        t += 1
        number += t
        factors = mydiv.prime_factors(number)
        num_of_fac = 1
        for ele in factors:
            num_of_fac *= ele[1] + 1
        if num_of_fac > 500:
            searching = False
    return number

print(calc())
