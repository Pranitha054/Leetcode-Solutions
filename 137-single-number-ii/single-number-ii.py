class Solution(object):
    def singleNumber(self, nums):
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for i,j in dic.items():
            if j==1:
                return i
