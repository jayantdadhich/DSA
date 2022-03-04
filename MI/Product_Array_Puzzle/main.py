def ProductExceptSelf(n, arr):
    temp_1 = [0]*n
    temp_2 = [0]*n
    temp_1[0] = 1
    temp_2[n-1] = 1
    for i in range(1, n):
        temp_1[i] = temp_1[i-1] * arr[i-1]
    for j in range(n-2,-1,-1):
        temp_2[j] = temp_2[j+1] * arr[j+1]
    for i in range(0,n):
        arr[i] = temp_1[i] * temp_2[i]
    return arr
n = int(input("Enter no of Elements"))
arr = []
print("Enter Elements")
for i in range(0, n):
    a = int(input(""))
    arr.append(a)
x = ProductExceptSelf(n, arr)
print(x)


