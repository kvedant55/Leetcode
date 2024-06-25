class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        for i in range(0,len(s)-1):

            a=ord(s[i])
            b=ord(s[i+1])
            res=res+abs((a-b))
        return res    