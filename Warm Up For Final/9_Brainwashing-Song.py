# Soal : Memisahkan setiap string dengan spasi setiap sebelum huruf kapital
S = input()

hasil = S[0]
for i in range(1, len(S)):
    if S[i].isupper():
        hasil += ' ' + S[i]
    else:
        hasil += S[i]
    
print(hasil)