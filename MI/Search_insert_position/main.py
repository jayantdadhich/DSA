def searchInsertK(n, k, arr):
       for i in range(0,n):
           if arr[i] == k:
               return i

n = int(input("Enter number of Elements"))
print("Enter Elements")
arr = []
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
k = int(input("Enter Element to search"))
i = searchInsertK(n, k, arr)
print(f"The Elements {k} is found at {i} ")