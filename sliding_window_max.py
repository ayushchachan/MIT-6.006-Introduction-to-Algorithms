from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        N = len(nums)
        Q = deque()
        Q.append(nums[0])
        answer = []

        for i in range(1, k):
            while len(Q) > 0 and Q[-1] < nums[i]:
                Q.pop()
            Q.append(nums[i])

        answer.append(Q[0])
        ## window is ready
        for i in range(k, N):
            if nums[i - k] == Q[0]:
                Q.popleft()
            while len(Q) > 0 and Q[-1] < nums[i]:
                Q.pop()
            Q.append(nums[i])

            answer.append(Q[0])
        return answer
