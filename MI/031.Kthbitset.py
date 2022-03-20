class Solution:
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        temp = []
        while n != 0:
            a = n % 2
            n = n // 2
            temp.append(a)
        for i in range(0, len(temp)):
            if temp[i] == 1 and k == i:
                return True
        return False