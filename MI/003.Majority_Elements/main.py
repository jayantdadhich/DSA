def MajorityElements(nums) :
    sums = {}
    for n in nums:
        if n not in sums:
            sums[n] = 1
        else:
            sums[n] = sums[n] + 1
        if sums[n] > len(nums)/2:
            return n

n = int(input("Enter number of elements in array"))
print("Enter Elements")
nums =[]
for i in range(0,n):
    a = int(input(""))
    nums.append(a)
x = MajorityElements(nums)
print(x)


