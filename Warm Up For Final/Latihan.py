# N = int(input())
# Kelas = ''
# Kluster = ''

# if N <= 0:
#     Kelas += 'A'
# elif 0 < N <= 100:
#     Kelas += 'B'
# elif 100 < N <= 200:
#     Kelas += 'C'
# else:
#     Kelas += 'D'

# if N % 3 == 0:
#     Kluster += '1'
# elif N % 3 == 1:
#     Kluster += '2'
# elif N % 3 == 2:
#     Kluster += '3'

# print(Kelas + Kluster)



# def FPB(x, y):
#     minimum = min(x, y)

#     for i in range (1, minimum+1):
#         if ((x % i == 0) and (y % i == 0)):
#             fpb = i
    
#     return fpb

# def KPK(x, y):
#     kpk = (x * y) // FPB(x, y)

#     return kpk

# x, y = map(int, input().split())
# print(KPK(x, y))


N = map(int, input().split())

N_set = set(N)

print(list(N_set))