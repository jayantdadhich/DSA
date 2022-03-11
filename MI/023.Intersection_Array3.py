class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        c = set(a)
        d = set(b)
        return len(c & d)
