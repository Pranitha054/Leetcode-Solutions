class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        print(nums1)
