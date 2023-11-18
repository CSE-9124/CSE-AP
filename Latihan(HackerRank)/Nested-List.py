# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty: Easy

# ======================== Solution ========================

records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
        
    records.append([name, score])
        
findScore = [x[1] for x in records]
sortScore = sorted(set(findScore))
    
findName = []
for y in records:
    if y[1] == sortScore[1]:
        findName.append(y[0])
            
for i in sorted(findName):
    print(i)