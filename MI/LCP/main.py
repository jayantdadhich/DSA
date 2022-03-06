def LCP(n, arr):
    min = len(arr[0])
    temp1 = arr[0]
    for i in range(0,len(arr)):
        if len(arr[i]) < min:
            min = len(arr[i])
            temp1 = list(arr[i])
    temp2 = temp1
    count = 0
    a = []
    for i in arr:
        if i[0] != temp2[0]:
            return []
        else:
            for j in range(0, min):
                if i[j] == temp2[j]:
                    count = count + 1
    r = count//n
    for i in range(0, r):
        a.append(temp2[i])
    return a

n = int(input("Enter number of strings in an array."))
arr = []
print("Enter elements of array.")
for i in range(n):
    a = input("")
    arr.append(a)
x = LCP(n, arr)
print(x)



