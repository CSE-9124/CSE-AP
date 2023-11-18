''' # Pemanggilan Fungsi
def printHello():
    print('Hello World')
printHello()

def tambah(a,b):
    return a + b
print(tambah(3,4))
'''

# Fungsi dengan Parameter
'''# 1. Default Argument
def greet(name ='Guest'):
    print(f'Hello, {name}')

greet()
greet('Cholyn')'''

'''# 2. Keyword Arguments (Memanggil fungsi dengan menyebutkan nama parameter beserta nilainya, Tanpa harus berurutan)
def describe_pet(name, animal_type):
    print(f'{name} is a {animal_type}.')

describe_pet(animal_type = 'cat', name = 'Yuta')'''

'''# 3. Positional Arguments (argument yang diberikan berdasarkan urutan parameter yg telah didefinisikan)
def greet(name, age):
    print(f'Hello, my name is {name} and I am {age} years old')

greet('Franklin', 18)'''

'''# 4. Arbitrary Arguments (Membuat fungsi yang bisa menerima banyak nilai tanpa batasan)
# Contoh *args (Mengumpulkan nilai-nilai argument dalam bentuk Tupel)
def add(*args):
    total = sum(args)
    return total

print(add(1, 2, 3, 4, 5))

# Contoh **kwargs (Mengumpulkan nilai-nilai argument dalam bentuk Dictionary)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

show_info(name = 'Alice', age = 30, tahun = 2023)

# Contoh Kombinasi *args dan **kwargs
def tampilkan_data(*args, **kwargs):
    print('data :')
    for data in args:
        print(data)
    print('Informasi Tambahan :')
    for kunci, nilai in kwargs.items():
        print(f'{kunci}: {nilai}')

tampilkan_data('Cholyn', 'Billy', 'Abel', hobi = "Gamers", kota = 'Makassar')'''
# Tidak harus menggunakan *args dan **kwargs tetapi bisa menggunakan kata lain selama ada tanda (*) dan (**) 


# Fungsi Rekursif (Memanggil dirinya sendiri dalam bodynya, dapat menghasilkan Perulangan Terbatas dan Perulangan Tanpa Batas)
'''# Contoh Perulangan Terbatas :
def show_intervals(start, end):
    print(start, end=' ')
    start += 1
    if start <= end:
        show_intervals(start, end)

show_intervals(1, 10) '''

'''# Contoh Perulangan Tanpa Batas :
def show_multiple(value):
    print(value)
    value = value + value
    show_multiple(value)

show_multiple(1)'''

'''# Contoh Faktorial dengan Rekursi :
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = 5
result = factorial(n)
print(f'{n}! : {result}')'''

# Type Hinting pada Fungsi
'''def divide(a: float, b: float) -> float:
    return a / b

result = divide(10.0, 2.0)
print(result)'''

# Exception Handling
'''# 1. Docstring dalam Fungsi 
def docString():
    """
    Ini adalah contoh dari Docstring
    """
    pass

help(docString)'''

'''# 2. Penggunaan Pernyataan Try dan Except
def pembagian(a,b) -> float:
    try:
        return a / b
    except:
        return 'Pembagian dengan angka nol tidak diperbolehkan'
    
print(pembagian(1,0))'''

'''# 3. Penggunaan Raise
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Pesan Errorr')
    
    return a / b

divide(10,0) '''

'''# 4. Penggunaan Else dan Finally
a = int(input('a = '))
b = int(input('b = '))
try:
    hasil = a / b

except ZeroDivisionError:
    print('Error: Pembagian dengan angka nol tidak diizinkan!')

else:
    print('Hasil Pembagian:', hasil)

finally:
    print('Proses Selesai') '''

