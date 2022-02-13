def MissingNumber(array,n):
    total = (n+1)*(n+2)/2
    #sum_of_elements = sum(array)
    sum_of_elements = 0
    for i in array:
        sum_of_elements += i
    return total - sum_of_elements

n = int(input("Enter number of Elements"))
print("Enter Elements")
array = []
for i in range(0,n):
    a = int(input(""))
    array.append(a)
miss = MissingNumber(array, n)
print(f"Missing Element is {int(miss)}")








