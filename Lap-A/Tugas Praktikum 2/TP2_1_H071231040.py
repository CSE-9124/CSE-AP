# Soal Nomor 1 : Menghitung BMI yang dibedakan berdasarkan gendernya
print('''Pilih Gender Anda
1. Pria 
2. Wanita''')
choice = int(input('= '))
if choice != 1 and choice != 2:
    print('Gender Tidak Valid')
    exit() 

Tinggi = float(input('Masukkan tinggi badan (cm) : '))
Berat = float(input('Masukkan berat badan (kg) : '))

Tinggi /= 100 # Ubah Tinggi badan dari cm ke m

BMI = Berat / (Tinggi)**2

print()
if choice == 1:
    if BMI < 18:
        print(f'Anda Tergolong Underweight dengan BMI {BMI:.2f}')
    elif 18 <= BMI < 24 :
        print(f'Anda Tergolong Normal dengan BMI {BMI:.2f}')
    elif 24 <= BMI < 27 :
        print(f'Anda tergolong Overweight dengan BMI {BMI:.2f}')
    else:
        print(f'Anda tergolong Obese dengan BMI {BMI:.2f}')
elif choice == 2:
    if BMI < 17:
        print(f'Anda Tergolong Underweight dengan BMI {BMI:.2f}')
    elif 17 <= BMI < 24 :
        print(f'Anda Tergolong Normal dengan BMI {BMI:.2f}')
    elif 24 <= BMI < 28 :
        print(f'Anda tergolong Overweight dengan BMI {BMI:.2f}')
    else:
        print(f'Anda tergolong Obese dengan BMI {BMI:.2f}')
else:
    print('Gender Tidak Valid')