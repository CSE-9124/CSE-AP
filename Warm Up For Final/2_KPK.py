def FPB(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            fpb = i

    return fpb

def KPK(x, y):
    kpk = (x * y) // FPB(x, y)
    
    return kpk

x, y = map(int, input().split())
print(KPK(x, y))