# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/sepatu-di-toko
# Difficulty: Easy

# ======================== Solusi ========================

def Banyak_Jumlah_Pasang(N, ListOfN):
    Pasang = 0
    Banyak_Ukuran = {}

    for Size in ListOfN:
        if Size in Banyak_Ukuran:
            Banyak_Ukuran[Size] += 1
        else:
            Banyak_Ukuran[Size] = 1

    for count in Banyak_Ukuran.values():
        Pasang += count // 2

    return Pasang


N = int(input())
ListOfN = list(map(int, input().split()))

M = Banyak_Jumlah_Pasang(N, ListOfN)
print(M)


# ======================== Test Case ========================
''' Test Case 0 '''
N = 6
ListOfN = [21, 21, 21, 30, 34, 34]
M = Banyak_Jumlah_Pasang(N, ListOfN)
print(M)

''' Test Case 1 '''
N = 9
ListOfN = [40, 34, 34, 20, 20, 40, 42, 41, 42]
M = Banyak_Jumlah_Pasang(N, ListOfN)
print(M)

''' Test Case 2 '''
N = 100
ListOfN = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 
           54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 
           23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 
           60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 
           43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]
M = Banyak_Jumlah_Pasang(N, ListOfN)
print(M) # Output : 30

''' Test Case 3 '''
N = 100
ListOfN = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
           42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
           42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
           42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
           42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
M = Banyak_Jumlah_Pasang(N, ListOfN)
print(M) # Output : 50