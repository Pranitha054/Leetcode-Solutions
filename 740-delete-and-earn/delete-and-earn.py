class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        prev2 = 0
        prev1 = 0
        for i in range(1, mx + 1):
            curr = max(prev1, prev2 + i * freq[i])
            prev2 = prev1
            prev1 = curr
        return prev1