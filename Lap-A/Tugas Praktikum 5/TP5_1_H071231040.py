s1 = input('s1 = ').replace(' ', '')
s2 = input('s2 = ').replace(' ', '')[::-1]
s3 = ''
p = min(len(s1), len(s2))

# CARA 1: Mengunakan For Loop
for i in range(p):
    mixed = s1[i] + s2[i]
    s3 += mixed

s3 += s1[p:] + s2[p:]

print(f'Hasil mixed = "{s3}"')

# CARA 2: Menggunakan def
def Mixed(s1,s2):
    s3 = ''
    terpendek = min(len(s1), len(s2))

    for i in range(terpendek):
        mix = s1[i] + s2[i]
        s3 += mix
    
    s3 += s1[terpendek:] + s2[terpendek:]
    return s3

print(f'Hasil mixed = "{Mixed(s1, s2)}"')

# CARA 3: Menggunakan While Loop
i = 0
while i < len(s1) and i < len(s2):
    s3 += s1[i] + s2[i]
    i += 1
s3 += s1[i:] + s2[i:]

print(f'Hasil mixed = "{s3}"')