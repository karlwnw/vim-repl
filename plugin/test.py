def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


gcd(12, 20)
