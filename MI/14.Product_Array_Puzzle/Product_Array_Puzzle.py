# By Division Method
def ProductExceptSelf(n, arr):
    temp = 1
    for i in range(0, n):
        temp = temp * arr[i]

    for i in range(0, n):
        arr[i] = temp/arr[i]
    return arr

n = int(input("Enter no of Elements"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = ProductExceptSelf(n, arr)
print(x)


