# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/swap-case/problem
# Difficulty: Easy

# ======================== Solution ========================

def swap_case(s):
    modify_s = ''
    for i in s:
        if i.isupper():
            modify_s += i.lower()
        else:
            modify_s += i.upper()
    return modify_s

s = input()
result = swap_case(s)
print(result)