N = input()

jumlah_digit_pembagi = 0
for i in N:
    if i != '0' and int(N) % int(i) == 0:
        jumlah_digit_pembagi += 1
        
print(jumlah_digit_pembagi)