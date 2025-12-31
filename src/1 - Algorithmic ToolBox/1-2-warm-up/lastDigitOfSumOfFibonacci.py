n = int(input())

def lastDigitOfSumOfFib(n):
    x = 0
    y = 1
    answer = 1
    for i in range(1, n):
        # print(y, end = " ")
        temp = y
        y = (x + y) % 10
        x = temp

        answer = (answer + y) % 10
    return answer

print(lastDigitOfSumOfFib(n))