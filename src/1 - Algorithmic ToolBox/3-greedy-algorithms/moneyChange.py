
money= int(input())

numTen = money // 10

money = money - (10 * numTen)

numFive = money // 5
money = money - (5 * numFive)
print(numFive + numTen + money)