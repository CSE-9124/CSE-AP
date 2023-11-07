print('Selamat datang untuk memulai silahkan input data anda')

Data = {
    'Nama' : '',
    'Umur' : '',
    'Alamat' : ''
}
 
Data['Nama'] = input('Input nama: ')
Data['Umur'] = input('Input umur: ')
Data['Alamat'] = input('Input alamat: ')

while True:
    print(f'''
=====================================================
Selamat datang {Data['Nama']} silahkan pilih opsi
===================================================== 
1. Detail anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar ''')

    print('=====================================================')
    opsi = input('Input opsi : ')
    print('=====================================================')

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
    else:
        print("Opsi Invalid")
        break