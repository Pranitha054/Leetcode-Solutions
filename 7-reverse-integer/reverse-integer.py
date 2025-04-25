class Solution(object):
    def reverse(self, x):
        n=abs(x)
        reverse=0
        INT_MAX = 2**31 - 1
        while n>0:
            a=n%10
            reverse=(reverse*10)+a
            n=n//10
            if reverse>INT_MAX:
                return 0
        return reverse if x >= 0 else -reverse
        