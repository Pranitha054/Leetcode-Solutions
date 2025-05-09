class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        seen=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
        seen=sorted(list(seen))
        if len(seen)>=3:
            return seen[-3]
        else:
            return seen[-1]
        

        