# 3. Melakukan Operasi pada Dictionary
dictExample = {
    "name": "Riofuad",
    "age": 21,
    "hobby": "Playing Genshin"
}

nestedDict = {
    "Fakultas": "MIPA",
    "Program Studi": {
        1: "Sistem Informasi",
        2: "Matematika",
        3: "Aktuaria"
    }
}

# a. Mengakses Elemen               -> ".get()"
# untuk mengakses elemen pada dictionary, harus merujuk pada nama key-nya. 
print(dictExample["name"])
    # menggunakan .get()
print(dictExample.get("name"))

# untuk mengakses elemen yg ada pada nested dictionary, harus merujuk pada nama key yang diluar hingga key yang paling dalam
print(nestedDict["Program Studi"][1])
    # menggunakan .get()
print(nestedDict.get("Program Studi").get(1))


# b. Mengupdate/Menambah Elemen      -> ".update()"
print("Before:", dictExample["hobby"])

# untuk mengupdate elemen pada dictionary kita hanya perlu mengintansinya kembali 
dictExample["hobby"] = "Playing Minecraft"
print("After:", dictExample["hobby"])
    # menggunakan .update()
dictExample.update({"hobby": "Playing GTA Online"})
print("After:", dictExample["hobby"])

# begitu pula untuk menambah elemen pada dictionary
dictExample["graduationYear"] = 2023
print(dictExample)
    # menggunakan .update()
dictExample.update({"graduationYear": 2026})
print(dictExample)


# c. Menghapus Elemen
# ~ Pop         -> ".pop()"     (utk menghapus elemen pada key yg spesifik)
dictExample.pop("graduationYear")
print(dictExample)

# ~ Popitems    -> ".popitem()"    (utk menghapus elemen yang terdapat pada akhir daftar)
dictExample.popitem()
print(dictExample)

# ~ Clear       -> ".clear()"    (utk menghapus seluruh elemen)
dictExample.clear()
print(dictExample)