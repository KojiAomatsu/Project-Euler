import sympy

def calc():
    result = 1
    score = 1
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            prime = True
            i = -1
            while prime:
                i += 1
                prime = sympy.isprime(i**2+a*i+b)
            if i > score:
                score = i
                result = a*b
            prime = True
    return result

print(calc())
