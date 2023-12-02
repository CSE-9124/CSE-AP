# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Difficulty: Easy

# ======================== Solution ========================
# CARA 1 :
def birthdayCakeCandles(candles):
    return candles.count(max(candles))

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

print(birthdayCakeCandles(candles))


# CARA 2 :
from collections import defaultdict

def birthdayCakeCandles(candles):

    #create a default with a default factory of integers
    hash_table = defaultdict(int) 
		
    for candle in candles:
        hash_table[candle] += 1
        
    return max(hash_table.values())

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

print(birthdayCakeCandles(candles))


# ======================== Test Case ========================
candles_count = 4
candles = [3, 2, 1, 3]
print(birthdayCakeCandles(candles))

candles_count = 4
candles = [4, 4, 1, 3]
print(birthdayCakeCandles(candles))