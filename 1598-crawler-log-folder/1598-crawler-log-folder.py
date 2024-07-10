class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in logs:
            a=ord(i[0])
            if((a>=67 and a<=122) or (a>=48 and a<=57)):
                count=count+1
            elif(i[0:2]==".."):
                if(count>0):

                    count=count-1
        if(count<0):
            count=0        
        return count           