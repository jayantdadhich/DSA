def find_height(n, x, arr):
    count = 0
    for i in range(0,n):
        if arr[i] == x:
            count = 0

        elif arr[i] <= x:
            count = 0

        else:
            y = arr[i] - x
            count = count + y
    return count

n = int(input("Enter number of Trees"))
x =int(input("Enter the height at which tree needs to be cut down"))
print("Height of each Tree")
arr = []
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
count = find_height(n, x, arr)
print(f"Wood collected by cutting trees are {count}")