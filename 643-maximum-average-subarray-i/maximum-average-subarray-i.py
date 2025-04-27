class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=sum(nums[:k])
        max_avg=window_sum/float(k)
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_avg=max(max_avg,window_sum/float(k))
        return max_avg


