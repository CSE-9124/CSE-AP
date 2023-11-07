def Faktorial(angka):
    if angka == 0 or angka == 1:
        return 1
    else:
        return angka * Faktorial(angka - 1)
    
N = int(input())

print(Faktorial(N))