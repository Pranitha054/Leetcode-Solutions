class Solution(object):
    def countAndSay(self, n):

        res = "1"                 

        for _ in range(n - 1):  
            temp = ""          
            count = 1             

            for i in range(len(res)):
                if i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                else:
                    temp += str(count) + res[i]
                    count = 1  
            res = temp  

        return res