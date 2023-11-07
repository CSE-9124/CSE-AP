# Soal 2 : Mengecek apakah sebuah inputan merupakan IPv4, IPv6 atau bukan keduanya
import re

def IPv4(teks):
    pola = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    cocok = re.match(pola, teks)

    if cocok:
        return True
    else:
        return False
    
def IPv6(teks):
    pola = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    cocok = re.match(pola, teks)

    return True if cocok else False

def IP_check(teks):
    for i in teks:
        if IPv4(i):
            print('IPv4')
        elif IPv6(i):
            print('IPv6')
        else:
            print('Bukan IP Address')


# TEKS 1
'''This line has trailing whitespace
121.203.197.20
2001:0db8:0000:0000:0000:ff00:0042:8329'''


n = int(input('Banyak Baris : '))

teks1 = []
for i in range(n):
    teks1.append(input())

print()
IP_check(teks1)


# TEKS 2
'''213.214.111.564
444.444.444.444 not an ip address
1050:0:0a:0:5:600:300c:326b'''

n = int(input('\nBanyak Baris : '))

teks2 = []
for i in range(n):
    teks2.append(input())

print()
IP_check(teks2)