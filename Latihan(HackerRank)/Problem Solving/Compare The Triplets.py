# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Difficulty: Easy

# ======================== Solution ========================

def compareTriplets(a, b):
    Score_Bob = 0
    Score_Alice = 0

    for i in range (3):
        if a[i] > b[i]:
            Score_Alice += 1
        elif a[i] < b[i]:
            Score_Bob += 1
        else:
            pass
    
    hasil = [Score_Alice, Score_Bob]

    return hasil


a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a, b)
print(' '.join(map(str, result)))


# ======================== Test Case ========================
a = [17, 28, 30]
b = [99, 16, 8]
result = compareTriplets(a, b)
print(' '.join(map(str, result)))