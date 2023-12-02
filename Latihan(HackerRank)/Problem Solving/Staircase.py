# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/staircase/problem
# Difficulty: Easy

# ======================== Solution ========================
# CARA 1 :
def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end='')
        print('#' * i)

n = int(input().strip())
staircase(n)


# CARA 2 :
def staircase(n):
    for i in range(1, x + 1):
        print(" " * (x - i) + "#" * i)

x = int(input())
staircase(n)