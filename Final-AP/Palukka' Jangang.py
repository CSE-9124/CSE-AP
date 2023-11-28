def count_value(nums):
    prev_max = 0
    curr_max = 0

    for num in nums:
        temp = curr_max
        curr_max = max(prev_max + num, curr_max)
        prev_max = temp

    return curr_max


nums = list(map(int, input().split()))
result = count_value(nums)
print(result)
