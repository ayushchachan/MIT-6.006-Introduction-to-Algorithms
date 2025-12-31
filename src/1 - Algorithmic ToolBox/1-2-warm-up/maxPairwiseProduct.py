nums = list(map(int, input().split()))

##method 1
nums.sort()

print(nums[-1] * nums[-2])