def indexes(n, arr, k):
    for i in range(n):
        if arr[i] == k:
            print(f"The First Index was found out at {i}")
            break
    arr.reverse()
    for j in range(n):
        if arr[j] == k:
            print(f" and the last index was found at {n-j-1}")
            break

n = int(input("Enter no of Elements"))
print("Enter Elements")
arr = []
for i in range(n):
    a = int(input(""))
    arr.append(a)
k = int(input("Enter the element which you want to find"))
arr = indexes(n, arr, k)

