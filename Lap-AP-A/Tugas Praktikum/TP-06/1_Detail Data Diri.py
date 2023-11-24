# Soal 1 : Membuat Program untuk Mengubah Data Detail Anda,

print('Selamat datang untuk memulai silahkan input data anda')

Data = {
    'Nama' : '',
    'Umur' : '',
    'Alamat' : ''
}

while True:
    Data['Nama'] = input('Input nama: ')
    if Data['Nama'].replace(' ', '').replace('.', '').isalpha() and len(Data['Nama'].replace(' ', '').replace('.', '')) > 0:
        break
    else:
        print('Nama Invalid!!!')

while True:
    Data['Umur'] = input('Input umur: ')
    if Data['Umur'].isdigit() and len(Data['Umur']) > 0 :
        break
    else:
        print('Umur Invalid!!!')

while True:
    Data['Alamat'] = input('Input alamat: ')
    if len(Data['Alamat']) > 0:
        break
    else:
        print('Alamat Invalid!!!')

while True:
    print(f'''
{'=' * 55}
Selamat datang {Data['Nama']} silahkan pilih opsi
{'=' * 55} 
1. Detail anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar ''')

    print('=' * 55)
    opsi = input('Input opsi : ')
    print('=' * 55)

    if opsi == '1':
       print(f'''Data anda adalah
Nama: {Data['Nama']}
Umur: {Data['Umur']}
Alamat: {Data['Alamat']}''') 
       
    elif opsi == '2':
        Namabaru = input('Silahkan Input nama baru: ')
        Data['Nama'] = Namabaru
        print('Data anda sukses diperbarui')

    elif opsi == '3': 
        Umurbaru = input('Silahkan Input umur baru: ')
        Data['Umur'] = Umurbaru
        print('Data anda sukses diperbarui')

    elif opsi == '4':
        Alamatbaru = input('Silakan Input alamat baru: ')
        Data['Alamat'] = Alamatbaru
        print('Data anda sukses diperbarui')

    elif opsi == '5':
        print(f"Selamat Tinggal {Data['Nama']}")
        break

    elif opsi.isalpha():
        print("Opsi Invalid")
        break

    else:
        print("Opsi Invalid")
        break