import os
import re

def Garis(n):
    return f'{"=" * n}'

def stringinbox(kata):
    return f"|{kata.center(50)}|"

def clear():
    os.system('cls')

while True:
    print(f'''{Garis(50):^52}
{stringinbox("Selamt Datang Silahkan Pilih Opsi Menu Anda")}
|{("-"*50):^50}|
{stringinbox("1. Detail Anda")}
{stringinbox("2. Ubah Nama")}
{stringinbox("3. Jumlah Data Pada Files")}
{stringinbox("4. Save Data Pada Files")}
{stringinbox("5. Buat Data Baru")}
{stringinbox("6. keluar")}
{Garis(50):^52}''')

    while True:
        inputan_penguna = int(input(f"|{'Masukan Opsi'.center(50)}|\n{Garis(50).center(50)}\n\t\t\t: "))
        if inputan_penguna in [i for i in range(1,7)]:
            clear()
            break
        else: raise NameError