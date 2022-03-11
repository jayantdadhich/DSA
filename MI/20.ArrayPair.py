class Solution:
	def canPair(self, nuns, k):
        if len(nuns)%2 == 1:
            return False
        
        for i in nuns:
            for  j in nuns:
                    temp = []
                    for i in nuns:
                        temp.append(i%k)
        temp = sorted(temp)
        for i in range(0, len(temp)):
            if (temp[i] + temp[len(temp)-i-1]) != k and (temp[i] + temp[len(temp)-i-1]) != 0:
                return False
        return True