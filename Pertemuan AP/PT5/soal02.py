def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

def permutasi(n,r):
    if n < r:
        return 0
    else:
        return faktorial(n) // faktorial(n-r)
    
n, r = (input().split(' '))
n = int(n)
r = int(r)
print(permutasi(n,r))    