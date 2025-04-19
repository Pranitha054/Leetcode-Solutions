class Solution(object):
    def isPalindrome(self, x):
        string=str(x)
        for i in range(len(string)):
            if (string[i])!=string[len(string)-i-1]:
                return False
        return True

        