def lcp(n, arr):
    rarr = []
    for i in arr:
        a = []
        for j in i:
            a.append(j)
        temp = a[0]
        a[0] = a[-1]
        a[-1] = temp
        str = ""
        for k in a:
            str = str + k
        rarr.append(str)
    return rarr

n = int(input("Enter number of strings in an array."))
arr = []
print("Enter string.")
for i in range(n):
    a = input("")
    arr.append(a)
x = lcp(n, arr)
print(x)



