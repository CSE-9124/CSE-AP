# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/palukka-jangang
# Difficulty: Easy

# ======================== Solusi ========================
# CARA 1 :
nums = list(map(int, input().split()))

def Palukka(nums):
    total_ganjil = 0
    total_genap = 0

    for i in range(len(nums)):
        if i % 2 == 0:  # posisi ganjil
            total_ganjil += nums[i]

        else:  # posisi genap
            total_genap += nums[i]

    return max(total_ganjil, total_genap)

print(Palukka(nums))


# CARA 2 :
nums = list(map(int, input().split()))

def count_value(nums):
    prev_max = 0
    curr_max = 0

    for i in nums:
        temp = curr_max
        curr_max = max(prev_max + i, curr_max)
        prev_max = temp

    return curr_max

print(count_value(nums))


# ======================== Test Case ========================
''' Test Case 0 '''
nums = [1, 2, 3, 1]
print(Palukka(nums))

''' Test Case 1 '''
nums = [1, 2, 2, 9, 1, 1]
print(count_value(nums))

''' Test Case 2 '''
nums = [1, 3, 4, 1]
print(Palukka(nums))

''' Test Case 3 '''
nums = [1, 3, 4, 2, 5]
print(count_value(nums))