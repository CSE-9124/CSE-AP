# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/collections-counter/problem
# Difficulty: Easy

# ======================== Solution ========================

from collections import Counter

X = int(input())
Shoe_Size = Counter(map(int, input().split()))

N = int(input())

Total = 0
for i in range(N):
    Size, Price = map(int, input().split())
    
    if Shoe_Size[Size]:
        Total += Price
        Shoe_Size[Size] -= 1

print(Total)