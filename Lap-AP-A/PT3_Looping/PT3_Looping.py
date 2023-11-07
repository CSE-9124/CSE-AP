'''# Penggunana While pada String
text = input()
index = 0

while index < len(text):
    print(text(index))
    index = index + 1 '''


'''# While loop bisa ditambakan statement else
n = int(input('Masukkan n : '))
jumlah = 0
i = 1

while i <= n:
    jumlah = jumlah + i
    i = i + 1
else:
    print(jumlah) '''


'''# Penggunaan If-Break pada while
i = 1

while i <= 5:
    print('6 * ', (i), '=', 6 * i)
    if i >= 3:
        break
    i = i + 1 '''


'''# Penggunaan If-Continue pada while 
num = 0

while num < 10:
    num = num + 1
    if num % 2 == 0:
        continue # digunakan untuk melangkahi angka yang habis dibagi 2 (bilangan genap)
    print(num) '''


# Penggunaan Nested Loop:
'''# For-For
adj = ['buah', 'enak']
fruits = ['apel', 'pisang']

for x in adj: # Loop Pertama
    for y in fruits: # Loop Kedua
        print(x,y) '''

'''# While-While
i = 1

while i <= 3: # Loop Pertama
    print(i)
    j = 1
    
    while j <= 2: #Loop Kedua
        print( j )
        j += 1
    
    i += 1 '''


'''# Penggunaan Try-Execption
x = 5
y = "Lima"

try:
    z = x+y
except:
    z = str(x)+y
else:
    print('Tidak dapat menjumlahkan kedua variable')
print(z) '''


# Study Case 1 :
# i = int(input())

# for m in range(i):
#     for j in range(m+1):
#         print('*', end="")
#     print()

# Study Case 2 :
# s = 0

# while True:
#     angka = int(input())

#     if angka < 0:
#         break
#     else:
#         s += angka
        
#     print(s)

# Study Case 3 :
# i = 0

# while i < 40:
#     i +=1
#     if i % 3 == 0:
#         continue

#     print(i)