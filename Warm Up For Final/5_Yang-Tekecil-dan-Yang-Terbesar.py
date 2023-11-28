# CARA 1:
N = sorted(list(map(int, input().split())))

print(f'{N[0]} {N[-1]}')


# CARA 2:
def maksimum(*angka):
    maks = angka[0]
    for angka_terbesar in angka:
        if angka_terbesar > maks:
            maks = angka_terbesar
    
    return maks

def minimum(*angka):
    mini = angka[0]
    for angka_terkecil in angka:
        if angka_terkecil < mini:
            mini = angka_terkecil
    
    return mini

N = list(map(int, input().split(' ')))

print(f'{minimum(*N)} {maksimum(*N)}')


# CARA 3:
def max_min(nums):
    max_num, min_num = nums[0], nums[0]

    for angka in nums:
        if angka > max_num:
            max_num = angka
        elif angka < min_num:
            min_num = angka

    return max_num, min_num

N = list(map(int, input().split(' ')))
print(max_min(*N))