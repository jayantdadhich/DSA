def Trailing_Zeroes(n):
    j = 5
    ans = 0
    while j <= n:
        ans = ans + n//j
        j = j*5
    return ans

n = int(input("Enter Number"))
print(Trailing_Zeroes(n))


