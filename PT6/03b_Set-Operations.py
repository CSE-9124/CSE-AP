# 6. Set Operations     (utk melakukan operasi Himpunan MTK)
# a. Union (⋃)          -> ".union()" or '|'
a = {1, 2, 3}
b = {3, 2, 1}
    # menggunakan |
print(a | b) # {1, 2, 3}
    # menggunakan .union()
print(a.union(b)) # {1, 2, 3}

# b. Intersection (⋂)   -> ".intersection()" or '&'
a = {1, 2, 3}
b = {3, 5, 1}
    # menggunakan &
print(a & b) # {1, 3}
    # menggunakan .intersection()
print(a.intersection(b)) # {1, 3}

# c. Difference (-)      -> ".difference()" or '-'
a = {1, 2, 5}
b = {3, 4, 1}
    # menggunakan -
print(a - b) # {2, 5}
    # menggunakan .difference()
print(a.difference(b)) # {2, 5}

# d. Symmetric Difference (^)   -> ".symmetric_difference()" or '^'
a = {1, 2, 5}
b = {3, 4, 1}
    # menggunakan ^
print(a ^ b) # {2, 3, 4, 5}
    # menggunakan .symmetric_difference()
print(a.symmetric_difference(b)) # {2, 3, 4, 5}
