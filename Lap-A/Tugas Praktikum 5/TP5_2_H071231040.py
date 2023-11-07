# Soal 2 : Mengambil Huruf pertama, tengah, dan akhir pada nama
Kata = input('Masukkan Kata: ')

# CARA 1
if len(Kata) % 2 == 0:
    hasil = Kata[0] + ' ' + Kata[-1]
    print(hasil)
else:
    hasil = Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
    print(hasil)


# CARA 2: Menggunakan def
def first_middle_last(kata):
    if len(kata) % 2 == 0:
        return kata[0] + '-' + kata[-1] 
    else:
        return kata[0] + kata[len(kata) // 2] + kata[-1]

kata = input('Masukkan Kata: ')
print(first_middle_last(kata))