def wave(n, arr):
    temp = 0
    for i in range(0, n, 2):
        temp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = temp
    return arr

n = int(input("Enter number of elements"))
print("Enter Elements")
arr = []
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = wave(n, arr)
print(x)
