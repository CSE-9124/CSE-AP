# Nomor 1
import os.path

name = input("Input nama File: ")
file_name = name[0] + name[len(name)//2] + name[-1]

folder_path = "Study Case"
file_path = folder_path + "/" + file_name + ".txt"

if os.path.exists(file_path):
    print(f"File {file_name}.txt already exist.")
else:
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_case = open(file_path, "w")
    file_case.write(f"Hello {name}")
    print(f"Successfully created {file_name}.txt file.")

file_case.close()