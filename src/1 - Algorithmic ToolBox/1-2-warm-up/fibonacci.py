n = int(input())

def fib(n):
    x = 0
    y = 1
    for i in range(1, n):
        # print(y, end = " ")
        temp = y
        y = x + y
        x = temp
        
    return y

print("fibonacci(", n, ") =", fib(n))