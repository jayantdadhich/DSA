def rotateArr(n,d,arr):
    for i in range(0,d):
        temp = arr[0]
        for j in range(0,len(arr)-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr
n = int(input("Enter number of Elements"))
d = int(input("How many rotation counter-clockwise you want to perform"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = rotateArr(n, d, arr)
print(x)

