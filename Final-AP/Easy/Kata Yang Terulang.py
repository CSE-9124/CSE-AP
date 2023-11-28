# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/mencari-yang-berulang
# Difficulty: Easy

# ======================== Solusi ========================

text = input().lower().split()

def Mencari_Kata_Terulang(text):
    duplikat = []
    for i in range(len(text)):
        for j in range(len(text)):
            if i == j:
                continue
            elif text[i] == text[j]:
                duplikat.append(text[i])
            else:
                continue

    if duplikat:
        duplikat = sorted(set(duplikat))
        return f'{set(duplikat)}\n{len(duplikat)}'
    else:
        return 'tidak ada kata berulang'

print(Mencari_Kata_Terulang(text))


# ======================== Test Case ========================
''' Test Case 0 '''
Text = 'the moon shone brightly in the night sky and stars twinkled around it like diamonds'.lower().split()
print(Mencari_Kata_Terulang(Text))

''' Test Case 1 '''
Text = 'in the garden colorful flowers bloomed and butterflies danced from one blossom to another'.lower().split()
print(Mencari_Kata_Terulang(Text))

''' Test Case 2 '''
Text = 'sky moon shone brightly in the night sky and stars twinkled around it like diamonds'.lower().split()
print(Mencari_Kata_Terulang(Text))