# Mode "r"
# file_test = open("test.txt", "r")

# isi_file = file_test.read()

# print(file_test.read())
# print(isi_file)


# Mode "w"
# file_test = open("test.txt", "w")

# file_test.write("Halo Dunia")


# Mode "r+"
# file_test = open("test.txt", "r+")

# print(file_test.read())

# file_test.seek(12)
# file_test.write("\nHalo3")

# print("after:")
# print(file_test.read())


# Mode "x"
# file_test = open("test3.txt", "x")
# file_test.write("Halo Halo Bandung")


# file_test = open("test.txt", "r")
# # file_test2 = open("test.txt", "r")

# print(file_test.read())
# print("Ini print line: ")
# file_test.seek(0)
# for i in range(5):
#     print(file_test.readline())

# print("Ini print lines: ")
# file_test.seek(0)
# print(file_test.readlines())

# file_test.close()

# print(file_test.readlines())

# with open("test.txt", "r") as file_test:
#     print(file_test.read())
#     print("Ini print line: ")
#     file_test.seek(0)
#     for i in range(5):
#         print(file_test.readline())

#     print("Ini print lines: ")
#     file_test.seek(0)
#     print(file_test.readlines())

# print(file_test.readlines())

import os

# print(os.getcwd())
# print(os.chdir("ini-folder"))

# print(os.listdir("ini-folder"))

# path_folder = "ini-folder"
# # path_folder2 = "ini-folder/file1.txt"

# path_file = os.path.join(path_folder, "file1.txt")
# print(path_file)

# with open(path_file, "r") as file_join:
#     print(file_join.read())

# path_folder = "ini-folder"
# path_file = os.path.join(path_folder, "file10.txt")

# if os.path.exists(path_file):
#     with open(path_file, "r") as file:
#         print(file.read())
# else:
#     with open(path_file, "x") as file:
#         file.write("Ini file yang baru di buat")

path_folder = "ini-folder"
path_file = os.path.join(path_folder, "file10.txt")

if not os.path.exists(path_file):
    os.mkdir(path_file)

else:
    os.remove(path_file)
