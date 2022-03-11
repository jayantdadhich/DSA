class Solution:
	def setBits(self, N):
		a = []
        while N > 0:
            temp = N % 2
            N = N // 2
            a.append(temp)
        count = 0
        for i in a:
            if i == 1:
                count += 1
        return count