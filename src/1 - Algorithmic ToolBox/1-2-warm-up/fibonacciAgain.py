

def pisanoPeriod(m):
    x = 0
    y = 1
    for i in range(1, m * m):
        # print(y, end = " ")
        temp = y
        y = (x + y) % m
        x = temp

        if y == 1 and x == 0:
            return i
    raise Exception()

def fib(n, m):
    x = 0
    y = 1
    for i in range(1, n):
        # print(y, end = " ")
        temp = y
        y = (x + y) % m
        x = temp
    return y

n, m = map(int, input().split())
p = pisanoPeriod(m)
print("pisano period is", p)
n2 = n % p
print(fib(n2, m))

# for i in range(2, 10):
#     print("i =", i, ", pisano =", pisanoPeriod(i))