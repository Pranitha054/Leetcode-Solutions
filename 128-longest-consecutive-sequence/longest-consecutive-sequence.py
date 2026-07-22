class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_count = 0  
        for num in num_set:
            if num - 1 not in num_set:  
                count = 1
                while num + count in num_set:  
                    count += 1
                max_count = max(max_count, count)

        return max_count