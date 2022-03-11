import math
class Solution:
    def reverseBits(self,n):
        temp = []
        while n > 0:
            a = n % 2
            n = n // 2
            temp.append(a)
        sum = 0
        l = temp[::-1]
        for i in range(0, len(l)):
            sum = sum + l[i]*(2**i)
        return sum
        