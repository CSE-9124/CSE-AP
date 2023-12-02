# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/migratory-birds/problem
# Difficulty: Easy

# ======================== Solution ========================

def migratoryBirds(arr):
    bird_counts = {}

    # Count the occurrences of each bird type
    for bird_id in arr:
        bird_counts[bird_id] = bird_counts.get(bird_id, 0) + 1

    # Find the maximum frequency
    max_frequency = max(bird_counts.values())

    # Find the bird type with the maximum frequency and the smallest id
    most_frequent_bird = min((bird_id for bird_id, count in bird_counts.items() if count == max_frequency))

    return most_frequent_bird