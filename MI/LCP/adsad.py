# def LCP(n, arr):
#     min = len(arr[0])
#     temp1 = list(arr[0])
#     for i in range(1,len(arr)):
#         if len(arr[i]) < min:
#             min = len(arr[i])
#             temp1 = list(arr[i])
#     a = []
#     for i in range(0,len(arr)):
#         temp2 = []
#         for j in range(0, min):
#             if arr[i][j] == temp1[j]:
#                 a.append(temp1[j])
#                 temp1.append(arr[i][j])
#         return a

def LCP(n, arr):
    min = len(arr[0])
    temp = []
    for i in range(1,n):
        if len(arr[i]) < min:
            min = len(arr[i])
            temp = list(arr[i])
    temp1 = temp

    a = []
    # print(temp1)
    count = 0
    for j in arr:
        count +=1
        for k in range(0, min):
            if j[k] == temp1[k] and count == n:
                a.append(j[k])
                # print(j[k])
    return a