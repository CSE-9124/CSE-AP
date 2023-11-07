# CARA 1 :
def nilaiHuruf(x):
    x = float(x)
    if 85.00 <= x <= 100:
        return 'A'
    elif 80 <= x <= 84.99:
        return 'A-'
    elif 75 <= x <= 79.99:
        return 'B+'
    elif 70 <= x <= 74.99:
        return 'B'
    elif 65 <= x <= 69.99:
        return 'B-'
    elif 60 <= x <= 64.99:
        return 'C+'
    elif 50 <= x <= 59.99:
        return 'C'
    elif 40 <= x <= 49.99:
        return 'D'
    elif 0 <= x <= 39.99:
        return 'E'
    
print(nilaiHuruf(input()))


# CARA 2 :
def Nilai_Huruf(x):
    if 0 <= x <= 100.000:
        if 85.00 <= x <= 100:
            return 'A'
        elif 80 <= x <= 84.99:
            return 'A-'
        elif 75 <= x <= 79.99:
            return 'B+'
        elif 70 <= x <= 74.99:
            return 'B'
        elif 65 <= x <= 69.99:
            return 'B-'
        elif 60 <= x <= 64.99:
            return 'C+'
        elif 50 <= x <= 59.99:
            return 'C'
        elif 40 <= x <= 49.99:
            return 'D'
        else:
            return 'E'
    else:
        return 'Nilai tidak valid'

nilai = float(input())

print(Nilai_Huruf(nilai))