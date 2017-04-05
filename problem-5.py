import sympy
def the_least_common_multiple(n):
    result = {}
    for i in range(2, n+1):
        factor = sympy.factorint(i)
        for key in factor.keys():
            if key in result:
                if result[key] < factor[key]:
                    result[key] = factor[key]
            else:
                result[key] = factor[key]
        number = 1
        for key in result.keys():
            number *= key**result[key]
    return number

print(the_least_common_multiple(20))
