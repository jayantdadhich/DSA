def MajorityElement(nums):
    arr = sorted(nums)
    return len(arr)//2

n = int(input("Enter number of elements in array"))
print("Enter Elements")
nums =[]
for i in range(0,n):
    a = int(input(""))
    nums.append(a)
x = MajorityElement(nums)
print(x)