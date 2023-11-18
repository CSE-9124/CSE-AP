# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/simple-array-sum/problem
# Difficulty: Easy

# ======================== Solution ========================

def simpleArraySum(ar):
    return sum(ar)

ar = list(map(int, input().split()))

result = simpleArraySum(ar)

print(result)