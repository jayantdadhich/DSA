def find_max(n, arr):
    max = arr[0]
    for i in range(0,n-1):
        if arr[i] < arr[i+1]:
            max = arr[i+1]
    return max

n = int(input("Enter number of Elements"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = find_max(n, arr)
print(x)


