# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/staircase/problem
# Difficulty: Easy

# ======================== Solution ========================

def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end='')
        print('#' * i)