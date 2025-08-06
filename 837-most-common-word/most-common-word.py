from collections import Counter
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'\w+', paragraph.lower()) 
        freq = Counter(words)
        banned_set = set(banned)
        max_word = ''
        max_count = 0
        for word, count in freq.items():
            if word not in banned_set and count > max_count:
                max_word = word
                max_count = count
        return max_word
