# Find the First Non-Repeating Character
# Given a string, return the first non-repeating character. If all characters repeat, return "None".

def first_unique_char(s: str) -> str:
   freq = {}
   for char in s:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
   
   for char in s:
    if freq[char] == 1:
      return char
   return None

s = "swiss"
print(first_unique_char(s))
