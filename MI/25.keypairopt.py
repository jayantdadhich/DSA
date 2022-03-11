class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
	   s = set()
	   for i in range(0, n):
	       bal = x - arr[i]
	       if bal in s:
	           return True
	       s.add(arr[i])
	   return False
