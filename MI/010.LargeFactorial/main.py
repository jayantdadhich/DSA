def _factorial(n, arr):
    a = []
    for i in arr:
        k = 1
        for j in range(1,i+1):
            k = k*j
        a.append(k)
    return a

n = int(input("Enter number of Elements"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = _factorial(n, arr)
print(x)

