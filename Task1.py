# Find the Missing Number in an Array
# A list contains n distinct numbers taken from 0, 1, 2, ..., n, but one number is missing.
# Write a function to find the missing number.

def find_missing_number(arr: list) -> int:
  n = len(arr)
  expected_sum = (n*(n+1))/2
  actual_sum =sum(arr)
  return expected_sum - actual_sum

arr1 = [3,0,1]
missing_num = find_missing_number(arr1)
