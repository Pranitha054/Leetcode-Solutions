class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        t=list(t)
        for i in range(len(s)):
            if s[i] not in t:
                return False
            else:
                t.remove(s[i])
        else:
            return True

        