def find_max(n, arr):
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] <  arr[mid+1]:
            first = mid + 1
        else:
            last = mid - 1

n = int(input("Enter number of Elements"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = find_max(n, arr)
print(x)

