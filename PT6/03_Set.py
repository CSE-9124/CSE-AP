# Sets (immutable)
# 1. Membuat Sets       "{}"
# set tidak mempunyai urutan tertentu jika argumentnya campuran (susunannya bisa saja teracak)
setExample = {"Python", 1, 2, "Java"}
print(setExample)

# set tidak menerima item duplikat 
duplicateSet = {1, 3, 2, 3, 2, 3, 4}
print(duplicateSet)


# 2. Memanipulasi Set
# Set bisa dimanipulasi jika dilakukan konversi tipe data set ke list terlebih dahulu
print("Before:", setExample)
setToList = list(setExample)
setToList[0] = "C++"
setExample = set(setToList)
print("After:", setExample)


# 3. Mengambil Data dari Set
numberSet = {1, 2, 3, 4, 5}
setToList = list(numberSet)
print(setToList[1])

numberSet = {1, 2, 3, 4, 5}
for i in numberSet:     # utk mengambil semua data dlm set
    print(i)