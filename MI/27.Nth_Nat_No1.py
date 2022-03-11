class Solution:
    def findNth(self,N):
        start = 1
        ans = 1
        while(start != N):
            ans += 1
            if(str(start).find('9') != 1):
                start += 1
        return ans
        