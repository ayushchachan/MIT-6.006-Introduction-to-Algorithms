n = int(input())

def lastDigitFib(n):
    x = 0
    y = 1
    print("i =", 1, "last digit =", y)
    for i in range(1, n):
        temp = y
        y = (x + y) % 10
        x = temp

        print("i =", i + 1, "last digit =", y)
    return y

print("last digit of fib(", n, ") =", lastDigitFib(n))