a, b = map(int, input().split())

def gcd(a, b):
    while (b % a != 0):
        temp = b % a
        b = a
        a = temp
    return a

print("gcd of", a, "and", b, "=", gcd(a, b))