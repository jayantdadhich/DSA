def searchInsertK(n, k, arr):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1

n = int(input("Enter number of Elements"))
print("Enter Elements")
arr = []
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
k = int(input("Enter Element to search"))
i = searchInsertK(n, k, arr)
print(f"The Elements {k} is found at {i} ")