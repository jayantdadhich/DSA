def  diagonalsort(arr):
    for i in range(0,m-1):
        for j in range(0,n-1):
            if i < j:
                for k in range(0, n-j)
                if arr[i][j] < arr[i+1][j+1]:
                    temp = arr[i+1][j+1]
                    arr[i+1][j+1] = arr[i][j]
                    arr[i][j] = temp
            elif j < i:
                if arr[i][j] > arr[i+1][j+1]:
                    temp = arr[i+1][j+1]
                    arr[i+1][j+1] = arr[i][j]
                    arr[i][j] = temp
    return arr
m = int(input("Enter number of rows"))
n = int(input("Enter number of columns"))
out = []
print("Enter elements")
for i in range(0,m):
    row = []
    for j in range(0,n):
        a = int(input(""))
        row.append(a)
    out.append(row)
x = diagonalsort(out)
print(x)
#print(out)


