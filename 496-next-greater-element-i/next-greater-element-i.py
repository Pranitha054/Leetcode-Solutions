class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums1:
            if i in nums2:
                index=nums2.index(i)
            max_element=i
            value=True
            for j in range(index+1,len(nums2)):
                if nums2[j]>max_element:
                    result.append(nums2[j])
                    value=False
                    break
            if value:
                result.append(-1)
        return result
        