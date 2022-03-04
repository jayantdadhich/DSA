#Time Complexity = O(n)
#Space Complexity = O(1)

def indexes(n, arr, k):
    first = -1
    last = -1
    for i in range(n):
        if(k != arr[i]):
            continue
        if(first == -1):
            first = i
        last = i
    if(first != -1):
        print("First Occurance = ", first,"\n Last Occurance ",last)
    else:
        print("Not found")

n = int(input("Enter no of Elements"))
print("Enter Elements")
arr = []
for i in range(n):
    a = int(input(""))
    arr.append(a)
k = int(input("Enter the element which you want to find"))
arr = indexes(n, arr, k)

