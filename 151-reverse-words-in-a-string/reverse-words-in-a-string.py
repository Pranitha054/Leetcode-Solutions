class Solution(object):
    def reverseWords(self, s):
        lis = []
        char = ""
        
        for i in s:
            if i == " ":
                if char != "":
                    lis.append(char)
                    char = ""
            else:
                char += i
        
        if char != "":
            lis.append(char)
        
        return " ".join(lis[::-1])