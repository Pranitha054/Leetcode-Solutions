from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        p_count = Counter(p)
        s_count = Counter()
        window_len = len(p)
        for i in range(len(s)):
            s_count[s[i]] += 1
            if i >= window_len:
                if s_count[s[i - window_len]] == 1:
                    del s_count[s[i - window_len]]
                else:
                    s_count[s[i - window_len]] -= 1
            if s_count == p_count:
                res.append(i - window_len + 1)
        return res

        
                
                        

        