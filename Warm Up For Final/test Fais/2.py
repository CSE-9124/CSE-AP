x, y = map(int, input().split())
sets = {0}
sets1 = {0}
for i in range(0, 100, x):
    sets.add(i)
for j in range(0, 100, y):
    sets1.add(j)


x = sorted(sets1.intersection(sets))
print(x[1])