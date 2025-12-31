

#  Return last digit of squares upto fib(n)
def lastDigitSumSquareFib(n):
    x = 0
    y = 1
    result = 1
    for i in range(1, n):
        temp = y
        y = (x + y) % 10
        x = temp

        result = (result + y*y) % 10
        # print("result = ", result)
    return result

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

n = int(input())
p = pisanoPeriod(10)

quotient = n // p
remainder = n % p

answer = 0
answer = answer + lastDigitSumSquareFib(p)
answer = (answer * quotient) % 10
answer = answer + lastDigitSumSquareFib(remainder)
print(answer % 10)
