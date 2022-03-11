def frequency(arr, n):
    temp = {}
    lis = {}
    for i in arr:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] = temp[i] + 1
    for i in range(0, n):
        if i not in temp.keys():
            lis[i] = 0
        else:
            lis[i] = temp[i]
    return lis.values()

n = int(input("How many Elements are there in Array"))
print("Enter elements")
arr = []
for i in range(0, n):
    a = int(input(""))
    arr.append(a)
x = frequency(arr, n)
print(x)




