n, W = map(int, input().split())

items = []

for i in range(n):
    v, w = map(int, input().split())
    items.append((v, w))

def ratio(item):
    value, weight = item
    return value / weight

sorted_list = sorted(items, key = ratio, reverse=True)

myBagWeight = 0
myBagValue = 0
i = 0
while (myBagWeight < W) and i < n:
    v, wt = sorted_list[i]
    if (wt <= W - myBagWeight):
        myBagWeight += wt
        myBagValue += v
        i = i + 1
    else:
        myBagValue += ratio((v, wt)) * (W - myBagWeight)
        myBagWeight = W
print(myBagValue)