d = int(input())                                    ## city is d miles away
m = int(input())                                    ## my car can travel atmost m miles on a full tank
n = int(input())                                    ## number of stops in between
distances = list(map(int, input().split()))         ## distances [stop0, stop1, stop2, ....] from home city

## need to find minimum number of refills needed

distances.append(d)                                 ## final destination
## will always reach stop1

i = -1
lastCheckPoint = 0
fuelLeft = m

numRefills = 0

while i < n:
    i = i + 1
    nextCheckPoint = distances[i]
    distanceToBeTravelled = nextCheckPoint - lastCheckPoint
    if (distanceToBeTravelled > m):
        numRefills = -1
        break
    elif (fuelLeft < distanceToBeTravelled < m):
        numRefills += 1
        fuelLeft = m
    lastCheckPoint = nextCheckPoint
    fuelLeft = fuelLeft - distanceToBeTravelled
print(numRefills)
