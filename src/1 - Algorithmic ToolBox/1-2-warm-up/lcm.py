a, b = map(int, input().split())


def gcd(a, b):
    while (b % a != 0):
        temp = b % a
        b = a
        a = temp
    return a

def lcm(a, b):
    g = gcd(a, b)
    while g != 1:
        a = a // g
        g = gcd(a, b)
    return a * b
print("lcm of", a, "and", b, "=", lcm(a, b))