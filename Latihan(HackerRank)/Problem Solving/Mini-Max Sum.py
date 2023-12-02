# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Difficulty: Easy

# ======================== Solution ========================
# CARA 1 :
def miniMaxSum(arr):
    mt = []
    for i in arr:
        mt.append(sum(arr) - i)
        
    print(min(mt), max(mt))

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)


# CARA 2 :
def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr)-arr[-1]
    max_sum = sum(arr)-arr[0]
    print(min_sum,max_sum)

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)


# ======================== Test Case ========================
arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)