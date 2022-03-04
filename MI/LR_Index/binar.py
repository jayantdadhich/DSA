def first(n, arr, k):
    low = 0
    high = n - 1
    res = -1
    while( low <= high):
        mid = (low + high)//2
        if arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res
def last(n, arr, k):
    low = 0
    high = n - 1
    res = -1
    while( low <= high):
        mid = (low + high)//2
        if arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res

n = int(input("Enter no of Elements"))
print("Enter Elements")
arr = []
for i in range(n):
    a = int(input(""))
    arr.append(a)
k = int(input("Enter the element which you want to find"))
a = first(n, arr, k)
b = last(n, arr, k)
print(f"The first Index is {a} and last index is {b}")

