class Solution(object):
    def removeOuterParentheses(self, s):
        sol=""
        res=""
        count1=0
        count2=0
        for i in s:
            if i=="(":
                count1+=1
                res+=i
            else:
                count2+=1
                if count1==count2:
                    res=res[1:]
                    sol+=res
                    res=""
                    count1=0
                    count2=0
                else:
                    res+=i
        return sol
        
        
