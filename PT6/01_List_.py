# 1. Membuat List        "[]"
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

rangeList = list(range(1, 9, 2))
print(rangeList)

# 2. Mengakses Data List
# ~ Mengambil elemen pertama
print(listExample[0])   # output -> 1

# ~ Mengambil elemen terakhir
print(listExample[len(listExample) - 1])    # output -> 3

# ~ Menginisialisasi nilai list pada indeks yang ingin diubah
listExample[1] = 10
print(listExample)      # output -> [1, 10, 3]