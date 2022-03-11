class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        c = []
        for i in a:
            c.append(i)
        for j in b:
            c.append(j)
        count = 0
        d = dict()
        for k in range(0, m+n):
            d[k] = c.count(c[k])
        for key, value in d.items():
            if value != 1:
                count  += 1
        return count//2