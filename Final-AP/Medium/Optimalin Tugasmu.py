# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/optimalin-tugasmu
# Difficulty: Medium

# ======================== Solusi ========================

N = int(input())
Tugas = []
for i in range(N):
    Tugas.append(list(map(int, input().split())))

def Optimal_Tugas(N, Tugas):
    # Mengurutkan tugas berdasarkan tingkat kesulitan (Di) secara menurun
    Tugas_sorted = sorted(Tugas, key=lambda x: x[1], reverse=True)

    # Mengurutkan tugas berdasarkan waktu penyelesaian (Ti) secara menaik
    Tugas_sorted = sorted(Tugas_sorted, key=lambda x: x[0])

    # Mendapatkan urutan optimal berdasarkan indeks tugas
    urutan_optimal = [t[0] for t in Tugas_sorted]

    return urutan_optimal

hasil = Optimal_Tugas(N, Tugas)
print(*hasil)