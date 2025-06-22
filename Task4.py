# Longest Consecutive Sequence
# Given an unsorted list of integers, find the length of the longest consecutive sequence.

def longest_consecutive(nums: list) -> int:
    num_set = nums
    longest = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count the streak
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))
