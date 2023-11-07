print('Mencoba Kode')
import os

os.system('cls')

import re

teks = 'System Analyst, Software Developer, '
Pola = r'[A-Za-z]{6,8}\s[A-Za-z]{7,9}(,)'
cocok = re.findall(Pola, teks)

print(cocok)

Teks = 'System Analyst, Software Developer, Konsultan IT, Cyber Security, Database Administrator, IT Project Manager, dan Konsultan Sistem Informasi.'
Pola = r'[A-Za-z]{5,9}\s[A-Za-z]{2,13}|, '
cocok = re.findall(Pola, Teks)

print(cocok)