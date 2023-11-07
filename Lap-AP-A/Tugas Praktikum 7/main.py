import datetime
import random
import os

# Minta input dari pengguna
nama_kasir = input("Masukkan nama kasir: ")
produk = []
while True:
    nama_produk = input("Masukkan nama produk (kosongkan untuk selesai): ")
    if not nama_produk:
        break
    harga = int(input("Masukkan harga produk: "))
    jumlah = int(input("Masukkan jumlah produk yang akan dibeli: "))
    produk.append({"nama": nama_produk, "harga": harga, "jumlah": jumlah})

# Hitung total harga
total_harga = sum([p["harga"] * p["jumlah"] for p in produk])

# Buat ID transaksi
inisial_kasir = nama_kasir[0].upper()
waktu_sekarang = datetime.datetime.now()
id_transaksi = f"{inisial_kasir}{waktu_sekarang.strftime('%y%m%d%H%M%S')}{random.randint(100, 999)}"

# Buat file invoice
nama_file = f"{id_transaksi}.txt"
folder_invoices = "invoices"
if not os.path.exists(folder_invoices):
    os.makedirs(folder_invoices)
path_file = os.path.join(folder_invoices, nama_file)
with open(path_file, "w") as f:
    f.write(f"ID Transaksi: {id_transaksi}\n")
    f.write(f"Nama Kasir: {nama_kasir}\n")
    f.write(f"Tanggal Transaksi: {waktu_sekarang.strftime('%d/%m/%Y %H:%M:%S')}\n")
    f.write("\n")
    f.write("Daftar Produk:\n")
    for p in produk:
        f.write(f"{p['nama']} x {p['jumlah']} = {p['harga'] * p['jumlah']}\n")
    f.write("\n")
    f.write(f"Total Harga: {total_harga}")

# Cetak invoice ke layar
with open(path_file, "r") as f:
    print(f.read())
