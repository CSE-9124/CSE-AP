'''Collection adalah kumpulan dari beberapa nilai baik itu angka, string, boolean,
bahkan variable dalam satu grub. Collection terbagi menjadi 4 yaitu: 
List, Tuples, Set dan Dictionary.'''

# A. List
'''# 1. Membuat List        "[]"
listExample = [1, 2, 3]
print(listExample)      # output -> [1, 2, 3]

blankList = []
print(blankList)        # output -> []

duplicateList = [1, 2, 2, 3, 1, 2, 4]
print(duplicateList)    # output -> [1, 2, 2, 3, 1, 2, 4]

mixedList = [1, 'Sistem', 'Informasi', 2023]
print(mixedList)        # output -> [1, 'Sistem', 'Informasi]

# Membuat list menggunakan 'range()'
rangeList = list(range(1, 5))
print(rangeList)        # output -> [1, 2, 3, 4]
'''

'''# 2. Mengakses Data List
# ~ Mengambil elemen pertama
print(listExample[0])   # output -> 1

# ~ Mengambil elemen terakhir
print(listExample[len(listExample) - 1])    # output -> 3

# ~ Menginisialisasi nilai list pada indeks yang ingin diubah
listExample[1] = 10
print(listExample)      # output -> [1, 10, 3]
'''

'''# 3. Slicing pada List  -> "[index_awal:index_akhir]"
ListExample = [0, 1, 2, 3, 4, 5, 6]
# Mengambil elemen yg dimulai dari awal hingga sebelum indeks tertentu -> "[:index]"
print(ListExample[:5])

# Mengambil elemen yg dimulai dari awal hingga sebelum indeks tertentu dari akhir -> "[:-index]"
print(ListExample[:-1])

# Mengambil elemen dimulai dari indeks tertentu hingga akhir -> "[index:]"
print(ListExample[1:])

# Mwngambil seluruh elemen dengan ururtan terbalik -> "[::-1]"
print(ListExample[::-1])
'''

'''# 4. List Multi-Dimensi     (Digunakan sebagai repersentasi Matriks di MTK)
multiDimensionalList = [[1, 2], [2, 3]]
print(multiDimensionalList[0][1])
'''

# 5. Built-In Function pada List
Listexample = [1, 2, 3, 4]
'''# ~ Append      -> ".append()"  (Memungkinkan penambahan satu elemen per operasi di ujung list)
print()
print(f'Before : {Listexample}')
Listexample.append(5)
print(f'After : {Listexample}') '''

'''# ~ Insert      -> ".insert(position, value)"  (utk menambahkan elemen pada lokasi yang spesifik)
print()
print(f'Before : {Listexample}')
Listexample.insert(1, 10)
print(f'After : {Listexample}') '''

'''# ~ Extend      -> ".extend()"  (saat ingin menembahkan beberapa elemen sekaligus di ujung list dan hanya menerima argumen list)
print()
print(f'Before : {Listexample}')
Listexample.extend([6, 7, 8])
print(f'After : {Listexample}') '''

'''# ~ Remove      -> ".remove()"  (utk menghapus nilai elemen yang ditentukan)
print()
print(f'Before : {Listexample}')
Listexample.remove(10)
print(f'After : {Listexample}') '''

'''# ~ Pop         -> ".pop()"  (utk mengambil elemen dari daftar dan menyimpannya ke variable baru)
print()
print(f'Before: {Listexample}')
popList = Listexample.pop(7)
print(f'After: {Listexample}')
print(f'Pop Value: {popList}') '''

'''# ~ Reverse     -> ".reverse()"  (utk membalik urutan elemen dalam list secara permanen)
print()
print(f'Before: {Listexample}')
Listexample.reverse()
print(f'After: {Listexample}') '''

# 6. List Comprehension
# Syntax : newList = [expression(element) for element in oldList if condition]
'''evenSquare = [x**2 for x in range(1,11) if x % 2 == 0]
print(evenSquare)'''


# B. Tuples (immutable)
'''# 1. Membuat Tuple      "()"
tupleExample = ('Python', True, 1)
print(tupleExample)     # output -> ('Python', True, 1)
'''

'''# 2. Mengakses Nilai pada Tuple
programmingLang = ("Python", "Java", "Kotlin")
    # with indexing
print("With Indexing:")
print(programmingLang[0])
    # with unpacking
a, b, c = programmingLang
print("\nWith Unpacking:")
print(a)
print(b)
print(c)
'''

'''# 3. Manipulasi Tuple
# Tuple bisa dimanipulasi jika dilakukan konversi tipe data tuple ke list terlebih dahulu
tupleExample = ("Python", True, 1)

print("Before:", tupleExample)
tupleToList = list(tupleExample)
tupleToList[1] = False
tupleExample = tuple(tupleToList)
print("After:", tupleExample)
'''

'''# 4. Menghapus Tuple    -> "del()"
del tupleExample
print(tupleExample)     # output -> error'''


# C. Sets (immutable)
'''# 1. Membuat Sets       "{}"
    # set tidak mempunyai urutan tertentu jika argumentnya campuran (susunannya bisa saja teracak)
setExample = {"Python", 1, 2, "Java"}
print(setExample)
    # set tidak menerima item duplikat 
duplicateSet = {1, 3, 2, 3, 2, 3, 4}
print(duplicateSet)'''

'''# 2. Memanipulasi Set
# Set bisa dimanipulasi jika dilakukan konversi tipe data set ke list terlebih dahulu
print("Before:", setExample)
setToList = list(setExample)
setToList[0] = "C++"
setExample = set(setToList)
print("After:", setExample)
'''

'''# 3. Mengambil Data dari Set
numberSet = {1, 2, 3, 4, 5}
print(list(numberSet))

numberSet = {1, 2, 3, 4, 5}
for i in numberSet:     # utk mengambil semua data dlm set
    print(i)
'''

# 4. Built-In Function di Set
setExample = {'Java', 'Python', 1, 2}
'''# ~ Add         -> ".add()"
setExample.add('Kotlin')
print(setExample)'''

'''# ~ Pop         -> ".pop()"  (hanya mengambil dan menyimpan nilai int pertama/str pertama pada data set)
setExample.pop()
print(setExample)'''

'''# ~ Remove      -> ".remove()"
setExample.remove(1)
print(setExample)'''

'''# ~ Discard     -> ".discard()"  (utk menghapus nilai yg sama)
setExample.discard("Tes")
print(setExample)'''

'''# 5. Frozen Set
duplicateSet = {1, 3, 2, 3, 2, 3, 4}
print(setExample)'''

# 6. Set Operations     (utk melakukan operasi Himpunan MTK)
'''# a. Union (⋃)          -> ".union()" or '|'
a = {1, 2, 3}
b = {3, 2, 1}
    # menggunakan |
print(a | b) # {1, 2, 3}
    # menggunakan .union()
print(a.union(b)) # {1, 2, 3}'''

'''# b. Intersection (⋂)   -> ".intersection()" or '&'
a = {1, 2, 3}
b = {3, 5, 1}
    # menggunakan &
print(a & b) # {1, 3}
    # menggunakan intersection()
print(a.intersection(b)) # {1, 3}'''

'''# c. Difference (-)      -> ".difference()" or '-'
a = {1, 2, 5}
b = {3, 4, 1}
    # menggunakan -
print(a - b) # {2, 5}
    # menggunakan difference()
print(a.difference(b)) # {2, 5}'''

'''# d. Symmetric Difference (^)   -> ".symmetric_difference()" or '^'
a = {1, 2, 5}
b = {3, 4, 1}
    # menggunakan ^
print(a ^ b) # {2, 3, 4, 5}
    # menggunakan symmetric_difference()
print(a.symmetric_difference(b)) # {2, 3, 4, 5}'''


# D. Dictionary
'''# 1. Membuat Dictionary
dictExample = {
    "name": "Riofuad",
    "age": 21,
    "hobby": "Playing Genshin"
}
print(dictExample)'''

'''# 2. Nested Dictionary
nestedDict = {
    "Fakultas": "MIPA",
    "Program Studi": {
        1: "Sistem Informasi",
        2: "Matematika",
        3: "Aktuaria"
    }
}
print(nestedDict)'''

# 3. 


# Study Case 1
tuple1 = (4, 8, 7, 3, 9)
tuple2 = (3, 5, 2, 4, 3)

list1= list(tuple1)
list2= list(tuple2)

x = (list1[0] % list2[0], list1[1] % list2[1], list1[2] % list2[2], list1[3] % list2[3], list1[4] % list2[4],)
x = tuple(x)
print(x)


# Study Case 2
# Kara = input().replace(' ', '')
# a = Kara.count('A')
# p = Kara.count('p')
# l = Kara.count('l')
# e = Kara.count('e')
# i = Kara.count('i')

# dict = {
#     "A" : a,
#     "p" : p,
#     "l" : l,
#     'e' : e,
#     'i' : i
# }

# print(dict)

# Study Case 3
mat = {'Amanda', 'Budi', 'Charlie', 'David'}
pengpro = {'Budi', 'Eva', 'David', 'Fiona'}

x = mat - (mat & pengpro)
y = pengpro - (mat & pengpro)

# a
print(mat & pengpro)

# b
print(mat ^ pengpro)

# c
print(x)
print(y)