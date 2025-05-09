class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)  # Store the numbers in a set
        result = []
        
        # Loop through the full range of numbers (1 to n)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:  # If a number is missing, add it to the result
                result.append(i)
        
        return result
