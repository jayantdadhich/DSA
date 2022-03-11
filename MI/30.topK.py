import heapq
class Solution:
	def topK(self, nums, k):
	    ans = []
	    freq = dict()
	    for num in nums:
	        if num not in freq:
	            freq[num] = 1
	        else:
	            freq[num] += 1
	    for key,val in freq.items():
	        if len(ans) < k:
	            heapq.heappush(ans, [val, key])
	        else:
	            heapq.heappushpop(ans, [val, key])
	    return[key for val, key in ans]