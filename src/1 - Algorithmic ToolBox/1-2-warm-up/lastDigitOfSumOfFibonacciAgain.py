m, n = map(int, input().split())

def lastDigitOfSumOfFibAgain(m, n):
    x = 0
    y = 1
    answer = 0
    for i in range(1, m - 1):
        # print(y, end = " ")
        temp = y
        y = (x + y) % 10
        x = temp
    
    for i in range(n - m + 1):
        # print(y, end = " ")
        temp = y
        y = (x + y) % 10
        x = temp

        answer = (answer + y) % 10
    return answer

print(lastDigitOfSumOfFibAgain(m, n))