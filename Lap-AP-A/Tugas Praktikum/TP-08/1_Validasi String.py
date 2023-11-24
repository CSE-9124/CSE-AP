# Soal 1 : Mengecek dan memvalidasi sebuah string inputan dari user
import re

User = input()

# CARA 1:
print('CARA 1:')

def validasi_string(string):
    pola = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
    cocok = re.findall(pola, string)

    if len(string) == 45:
        if cocok:
            return True
        else:
            return False
    else:
        return False
        
result = validasi_string(User)
print(result)


# CARA 2:
print('\nCARA 2:')

pola = r'\A[a-zA-Z02468]{40}[13579\s]{5}\Z'
cocok = re.match(pola,User)

print('True' if len(User) == 45 and cocok else 'False')
