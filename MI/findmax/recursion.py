def find_max(n, arr, low, high):
    if low == high:
        return arr[low]
    if low == high - 1 and arr[low] <= arr[high]:
        return arr[high]
    if low == high - 1 and arr[low] > arr[high]:
        return arr[low]
    mid = (low + high)//2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    elif arr[mid] > arr[mid + 1]:
        return find_max(n, arr, low, mid-1)
    else:
        return find_max(n, arr, mid+1, high)

n = int(input("Enter number of Elements"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = find_max(n, arr, 0, n-1)
print(x)

