# Nomor 3
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


name = input("Input nama File: ")
file_name = name[0] + name[len(name)//2] + name[-1]

folder_path = "Study Case"
file_path = folder_path + "/" + file_name + ".txt"

if os.path.exists(file_path):
    print(f"File {file_name}.txt already exist.")
    file_case = open(file_path, "w")
    n = int(input("Masukkan jumlah suku: "))
    file_case.write(fibonacci(n))
    print(f"Successfully updated {file_name}.txt file.")

    file_case = open(file_path, "r")
    print(file_case.read())
else:
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_case = open(file_path, "w")
    file_case.write(f"Hello {name}")
    print(f"Successfully created {file_name}.txt file.")

file_case.close()

delete = input("Delete File (y/n): ").lower()
if delete == 'y':
    delete_file = input("Masukkan nama file: ")
    file_path = folder_path + "/" + delete_file + ".txt"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {delete_file}.txt successfully deleted.")
    else:
        print(f"File {delete_file}.txt not found.")
elif delete == 'n':
    print("Remove File canceled.")