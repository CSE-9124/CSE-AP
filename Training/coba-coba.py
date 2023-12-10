print('coba-coba')

# orang = { 'nama' : 'Guido van Rossum', 
#   'umur' : 60,
#   'kewarganegaraan': 'Belanda',
#   'tempat tinggal': 'Amerika' }

# for kunci, item in orang.items():
#   print (f"{kunci}: {item}")


# def stringPermutation(input_str):
#     try:
#         # Cek apakah input adalah string
#         if not isinstance(input_str, str):
#             raise TypeError("Input harus berupa string")

#         # Inisialisasi daftar untuk menyimpan permutasi
#         permutations = []

#         # Loop untuk menghasilkan permutasi
#         for i in range(len(input_str) + 1):
#             rotated_str = input_str[i:] + input_str[:i]
#             permutations.append(rotated_str)

#         # Gabungkan permutasi dalam satu baris dengan tanda '|'
#         result = " | ".join(permutations)

#         # Tampilkan hasil
#         print(result)
#     except TypeError as e:
#         print(f"Error: {e}")

# # Contoh penggunaan
# stringPermutation("Ayam")


# x = input('Input kata/kalimat: ')
# palindrom = True
 
# panjang_x = len(x)
 
# for i in range(panjang_x//2):
#   if (x[i] != x[panjang_x-i-1]):
#     palindrom = False
#     break
  
# if palindrom:
#   print(x,'adalah palindrome!')
# else:
#   print(x,'bukan palindrome!');


# x = [1, 2, 3, 4, 5, 6]
# print(x[::-1])

# angka = -9
# print(abs(angka))


# x = "Billy"
# print(x[-1])


# space(10)


# y = len(x)
# print(f'y {type(y)}')

# h = y // 2
# print(h)

# s1 = input('s1 = ').replace(' ', '')
# s2 = input('s2 = ').replace(' ', '')
# s2 = s2[::-1]
# s3 = ''
# p = min(len(s1), len(s2))

# for i in range(p):
#     mixed = s1[i] + s2[i]
#     s3 += mixed

# s3 += s1[p:] + s2[p:]  # Tambahkan sisa karakter dari s2 setelah p

# print(f'Hasil mixed = "{s3}"')


# Mengambil sebagian kata
def Maksimal_Kata(Kata, Panjang):
    if len(Kata) > Panjang:
        Kata = Kata[:Panjang] + "..."
    return Kata

def space(a):
    print('\n' * a)

def Batas(n):
    print("=" * n)

import os
def clear_terminal():
    os.system('cls')