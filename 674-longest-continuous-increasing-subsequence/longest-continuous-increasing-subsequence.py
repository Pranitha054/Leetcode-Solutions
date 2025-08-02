class Solution(object):
    def findLengthOfLCIS(self, nums):
        max_len=curr_len=1 if nums else 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr_len+=1
                max_len=max(curr_len,max_len)
            else:
                curr_len=1
        return max_len