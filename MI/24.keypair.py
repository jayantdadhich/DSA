class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
	    for i in range(0, n):
	        for j in range(i+1, n):
	            if x == arr[i] + arr[j]:
	                return "Yes"