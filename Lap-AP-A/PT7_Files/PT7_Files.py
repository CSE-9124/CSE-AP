# membuka sebuah berkas
# file1 = open("test.txt", "r")

# # membaca berkas
# read_content = file1.read()
# print(read_content)


# print('\nCara Kedua :')
# file = open("test.txt", "r")
# print (file.read())

# # Append
# file2 = open("test.txt", "a")
# file2.write('Halo dunia')



#os.rmdir()  -> utk menghapus folder
#os.remove() -> utk menghapus file


# Study Case 1:
# import os.path

# def first_middle_last(Kata):
#     if len(Kata) % 2 == 0:
#         hasil = Kata[0] + ' ' + Kata[-1]
#         return hasil
#     else:
#         hasil = Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
#         return hasil

# Kata = input('Masukkan Kata: ')
# folder_path = "Study Case"
# file_path = os.path.join(folder_path, f"{first_middle_last(Kata)}.txt")

# if os.path.exists(file_path):
#     print(f'File {first_middle_last(Kata)}.txt alredy exist')
# else:
#     if not os.path.exists(folder_path):
#         os.mkdir(folder_path)

#     file_case = open(file_path, 'w')
#     file_case.write(f'Hello {Kata}')
#     print(f'Successfully created {first_middle_last(Kata)}.txt file')
 
# file_case.close()


# Study Case 2:
# import os.path

# def fibonacci(n):
#     a, b = 0, 1
#     hasil = ""

#     if n == 0:
#         return hasil
#     elif n == 1:
#         hasil += str(a)
#         return hasil
#     else:
#         hasil += f"{a}, {b}"
#         for i in range(2, n):
#             c = a + b
#             hasil += f", {c}"
#             a, b = b, c
#         return hasil

# def file_name(Kata):
#     if len(Kata) % 2 == 0:
#         hasil = Kata[0] + ' ' + Kata[-1]
#         return hasil
#     else:
#         hasil = Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
#         return hasil

# Nama = input('Masukkan Nama: ')
# folder_path = "Study Case"
# file_path = os.path.join(folder_path, f"{file_name(Nama)}.txt")

# # cek file sudah ada atau tidak
# if os.path.exists(file_path):
#     # Kalo file ada ganti ke fibonacci
#     print(f"File {file_name(Nama)}.txt already exist.")
    
#     # Menambahkan Angka Fibonacci
#     file_case = open(file_path, "a")
#     n = int(input("Masukkan jumlah suku: "))
#     file_case.write(fibonacci(n))

#     print(f"Successfully updated {file_name(Nama)}.txt file.")
# else:
#     # kalo tidak ada bikin baru
#     # cek dlu folder sudah ada atau tidak
#     if not os.path.exists(folder_path):
#         os.mkdir(folder_path)

#     file_case = open(file_path, "w")
#     file_case.write(f"Hello {Nama}")
#     print(f"Successfully created {file_name(Nama)}.txt file.")

# file_case.close()


# Study Case 3:
import os.path

def fibonacci(n):
    a, b = 0, 1
    hasil = ""

    if n == 0:
        return hasil
    elif n == 1:
        hasil += str(a)
        return hasil
    else:
        hasil += f"{a}, {b}"
        for i in range(2, n):
            c = a + b
            hasil += f", {c}"
            a, b = b, c
        return hasil

def file_name(Kata):
    if len(Kata) % 2 == 0:
        hasil = Kata[0] + ' ' + Kata[-1]
        return hasil
    else:
        hasil = Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
        return hasil

Nama = input('Masukkan Nama: ')
folder_path = "Study Case"
file_path = os.path.join(folder_path, f"{file_name(Nama)}.txt")

if os.path.exists(file_path):
    print(f"File {file_name(Nama)}.txt already exist.")
    
    file_case = open(file_path, "a")
    n = int(input("Masukkan jumlah suku: "))
    file_case.write(fibonacci(n))

    print(f"Successfully updated {file_name(Nama)}.txt file.")

    file_case = open(file_path, "r")
    isi = file_case.read()
    print(isi)

else:
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_case = open(file_path, "w")
    file_case.write(f"Hello {Nama}")
    print(f"Successfully created {file_name(Nama)}.txt file.")

file_case.close()

delete = input('Delete File (y/n): ').lower()

if delete == 'y':
    delete_file = input('Masukkan Nama File: ')
    file_path = os.path.join(folder_path, f"{delete_file}.txt")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'File {delete_file}.txt successfully deleted.')
    else:
        print(f'File {delete_file}.txt not found.')
elif delete == 'n':
    print('Delete File canceled')