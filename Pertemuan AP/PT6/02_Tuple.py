# Tuples (immutable)
# 1. Membuat Tuple      "()"
tupleExample = ('Python', True, 1)
print(tupleExample)     # output -> ('Python', True, 1)


# 2. Mengakses Nilai pada Tuple
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


# 3. Manipulasi Tuple
# Tuple bisa dimanipulasi jika dilakukan konversi tipe data tuple ke list terlebih dahulu
tupleExample = ("Python", True, 1)

print("Before:", tupleExample)
tupleToList = list(tupleExample)
tupleToList[1] = False
tupleExample = tuple(tupleToList)
print("After:", tupleExample)


# 4. Menghapus Tuple    -> "del()"
# Tuple tidak dapat diubah dan oleh karena itu tidak dapat dilakukan penghapusan sebagian dari nilainya
'''del tupleExample
print(tupleExample)     # output -> error'''