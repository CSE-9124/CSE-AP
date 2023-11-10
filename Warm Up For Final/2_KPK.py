# CARA 1 :
x, y = map(int, input().split())

sets_x = set()
sets_y = set()

for i in range(0, 100, x):
    sets_x.add(i)
for j in range(0, 100, y):
    sets_y.add(j)

x = sorted(sets_x & sets_y)
print(x)
print(x[1])


# CARA 2 :
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