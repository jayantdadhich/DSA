class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        count = 0
        for i in a:
            if i in b:
                count += 1
        return count