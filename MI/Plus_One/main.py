def Plus_One(n, arr):
    for i in range(n-1,-1,-1):
        if arr[i] == 9:
            arr[i] = 0
        else:
            arr[i] += 1
            return arr
    return [1] + arr

n = int(input("Enter no of digits"))
arr = []
print("Enter digits")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = Plus_One(n, arr)
print(x)
