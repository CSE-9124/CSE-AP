# 3. Slicing pada List  -> "[index_awal:index_akhir]"
ListExample = [0, 1, 2, 3, 4, 5, 6]
# Mengambil elemen yg dimulai dari awal hingga sebelum indeks tertentu -> "[:index]"
print(ListExample[:5])

# Mengambil elemen yg dimulai dari awal hingga sebelum indeks tertentu dari akhir -> "[:-index]"
print(ListExample[:-1])

# Mengambil elemen dimulai dari indeks tertentu hingga akhir -> "[index:]"
print(ListExample[1:])

# Mwngambil seluruh elemen dengan ururtan terbalik -> "[::-1]"
print(ListExample[::-1])


# 4. List Multi-Dimensi     (Digunakan sebagai repersentasi Matriks di MTK)
multiDimensionalList = [[1, 2], [2, 3]]
print(multiDimensionalList[0][1])

multiDimensionalList = [[1, 2], [2, 3], [10], [4, 5]]
print(multiDimensionalList[2][1]) # Erorr
print(multiDimensionalList[3][0])
