def summ(a,b):
    temp1 = []
    temp2 = []
    while a != 0:
        x = a % 2
        a = a // 2
        temp1.append(x)
    while b != 0:
        y = b % 2
        b = b // 2
        temp2.append(y)
    s = 0
    for i in range(0, len(temp1)):
        s = s + temp1[i] * (2 ** i)
    for i in range(0, len(temp2)):
        s = s + temp2[i] * (2 ** i)  
    return s
a = int(input(""))
b = int(input(""))
print(summ(a,b))