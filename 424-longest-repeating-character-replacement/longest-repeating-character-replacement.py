class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        count = {}
        max_freq = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            if count[s[r]] > max_freq:
                max_freq = count[s[r]]
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len