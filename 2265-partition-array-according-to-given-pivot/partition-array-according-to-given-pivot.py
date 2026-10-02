class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        small=[]
        middle=[]
        large=[]
        for i in nums:
            if i<pivot:
                small.append(i)
            elif i==pivot:
                middle.append(i)
            else:
                large.append(i)
        nums[:]=small+middle+large
        return nums