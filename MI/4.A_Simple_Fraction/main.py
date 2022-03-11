def Fraction_to_Decimal(numerator, denominator):
    S = numerator//denominator
    rem = numerator % denominator
    if rem == 0:
        return S
    S = S + "."
    while rem != 0:
        x = rem * 10
        S = S + str(x/denominator)
        return S

num = int(input("Enter Numerator"))
denom = int(input("Enter Denominator"))
x = str(Fraction_to_Decimal(num, denom))
print(x)