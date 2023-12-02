# ======================== Information ========================
# Direct Link: https://tlx.toki.id/problems/gemastik-2022-pemrograman-penyisihan/A
# Difficulty: Easy

# ======================== Solution ========================

A, C = map(int, input().split())
B, D = map(int, input().split())

Kali_AD = A * D
Kali_BC = B * C

if Kali_AD == Kali_BC:
    print('sama')
elif Kali_AD > Kali_BC:
    print('lebih besar')
else:
    print('lebih kecil')