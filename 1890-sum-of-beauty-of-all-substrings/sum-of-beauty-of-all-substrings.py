from collections import Counter

class Solution(object):
    def beautySum(self, s):
        total = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                ch = ord(s[j]) - ord('a')
                freq[ch] += 1

                non_zero = [f for f in freq if f > 0]
                total += max(non_zero) - min(non_zero)
        return total
