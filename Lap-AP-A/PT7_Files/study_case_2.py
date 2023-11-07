# Nomor 2
import os.path

# Fungsi Fibonacci mengembalikan String
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

# Input Nama
name = input("Input nama File: ")
file_name = name[0] + name[len(name)//2] + name[-1] # Bkin nama file

folder_path = "Study Case" # Bikin Folder
file_path = folder_path + "/" + file_name + ".txt" # Bikin path ke file

# cek file sudah ada atau tidak
if os.path.exists(file_path):
    # Kalo file ada ganti ke fibonacci
    print(f"File {file_name}.txt already exist.")
    file_case = open(file_path, "w")
    n = int(input("Masukkan jumlah suku: "))
    file_case.write(fibonacci(n))
    print(f"Successfully updated {file_name}.txt file.")
else:
    # kalo tidak ada bikin baru
    # cek dlu folder sudah ada atau tidak
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_case = open(file_path, "w")
    file_case.write(f"Hello {name}")
    print(f"Successfully created {file_name}.txt file.")

file_case.close()