# 5. Built-In Function pada List
Listexample = [1, 2, 3, 4]

# ~ Append      -> ".append()"  (Memungkinkan penambahan satu elemen per operasi di ujung list)
print()
print(f'Before : {Listexample}')
Listexample.append(5)
print(f'After : {Listexample}') 

# ~ Insert      -> ".insert(position, value)"  (utk menambahkan elemen pada lokasi yang spesifik)
print()
print(f'Before : {Listexample}')
Listexample.insert(1, 10)
print(f'After : {Listexample}') 

# ~ Extend      -> ".extend()"  (saat ingin menembahkan beberapa elemen sekaligus di ujung list dan hanya menerima argumen list)
print()
print(f'Before : {Listexample}')
Listexample.extend([6, 7, 8])
print(f'After : {Listexample}') 

# ~ Remove      -> ".remove()"  (utk menghapus nilai elemen yang ditentukan)
print()
print(f'Before : {Listexample}')
Listexample.remove(10)
print(f'After : {Listexample}') 

# ~ Pop         -> ".pop()"  (utk mengambil elemen dari daftar dan menyimpannya ke variable baru)
print()
print(f'Before: {Listexample}')
popList = Listexample.pop(7)
print(f'After: {Listexample}')
print(f'Pop Value: {popList}') 

# ~ Reverse     -> ".reverse()"  (utk membalik urutan elemen dalam list secara permanen)
print()
print(f'Before: {Listexample}')
Listexample.reverse()
print(f'After: {Listexample}') 
