# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/plus-minus/problem
# Difficulty: Easy

# ======================== Solution ========================

def plusMinus(arr):
    Plus = [x for x in arr if x > 0]
    Zero = [x for x in arr if x == 0]
    Minus = [x for x in arr if x < 0]
    
    print(f"{(len(Plus) / len(arr)):.6}")
    print(f"{(len(Minus) / len(arr)):.6}")
    print(f"{(len(Zero) / len(arr)):.6}")

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)


# ======================== Test Case ========================
n = 6
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)