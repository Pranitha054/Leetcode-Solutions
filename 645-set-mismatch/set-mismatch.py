class Solution(object):
    def findErrorNums(self, nums):
        output = [0, 0]  # [duplicate, missing]
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1

        for i in range(1, n + 1):
            if count[i] == 2:
                output[0] = i  # duplicate first
            elif count[i] == 0:
                output[1] = i  # missing next

        return output
