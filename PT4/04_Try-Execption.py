# try :
#   print(x)
# except:
#   print('An exception occurred')


man = input('Enter a Number --> ')
try :
    man = int(man)
except ValueError:
    print('INVALID Input')


while True:
  y = input('Masukkan Angka : ')

  try:
    y = int(y)
    break
  except ValueError:
    print("Error!! : Anda harus memasukkan Angka")
    print()

print(2 + y)


# Program --> Menerima Input nama tapi tidak menerima '.' '/' ';'
symbol = ('.', '/', ';')

while True:
  nama = input('Enter Nama : ')
  invalid = 0

  for char in symbol:
    if char in nama:
      invalid += 1

  if invalid > 0:
    print('Invalid : nama tidak boleh ada ".", "/", ";"')
  
  else:
    break

print()
print('Welcome ' + nama)