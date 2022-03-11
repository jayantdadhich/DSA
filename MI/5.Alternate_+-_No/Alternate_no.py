def rearrange(d, arr):
    m = []
    n = []
    p = []
    for i in range(0,d):
        if arr[i] < 0:
            m.append(arr[i])
        else:
            n.append(arr[i])
    for i in range(0,len(n)):
        p.append(n[i])
        p.append(m[i])
    return p

n = int(input("Enter number of Elements"))
arr = []
print("Enter Elements")
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
x = rearrange(n, arr)
print(x)





