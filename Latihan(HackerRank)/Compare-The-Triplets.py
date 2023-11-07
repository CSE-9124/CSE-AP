def compareTriplets(a, b):
    bobScore = 0
    alisaScore = 0
    hasil = []
    for i in range (3):
        if a[i] > b[i]:
            alisaScore += 1
        elif a[i] < b[i]:
            bobScore += 1
        else:
            pass
    hasil.append(alisaScore)
    hasil.append(bobScore)
    return hasil


a = [17, 28, 30]
b = [99, 16, 8]
print (compareTriplets(a, b))
