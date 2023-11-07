import re

print('\nStudy Case 1 :')
Nomor = 'The phone number of agent is +62 821-8719-6003 or 263 129-4781-0173. Call soon!'
pola = r'(\+[0-9]{2} [0-9]{3}-[0-9]{4}-[0-9]{4}|[0-9]{2} [0-9]{3}-[0-9]{4}-[0-9]{4})'

cocok = re.findall(pola, Nomor)

for i in range(len(cocok)):
    print(f'Nomor Teepon ke-{i} {cocok[i]}')


print('\nStudy Case 2 :')
import os

with open("numbers.txt", 'w') as F :
    F.write('''Narukami
123-456-789
Amagi
897434312
Rise
987-654-321''')

with open("numbers.txt", 'r') as R :
    Teks = R.read()

pola = r'[0-9]{3}-[0-9]{3}-[0-9]{3}'
cocok = re.findall(pola, Teks)

for i in cocok:
    print(i)


print('\nStudy Case 3 :')
x = '''www.amazon.com
linkgadung.id
www.YouTube.com'''

pola = r'[w]{3}\.([A-Za-z]+)\.com'

cocok = re.findall(pola,  x)
print(cocok)

for i in cocok:
    print(i)