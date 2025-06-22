# Valid Parentheses Checker
# Write a function to check whether a given string containing only (), {}, [] is balanced.

def is_valid(s: str) -> bool:
  stack = []
  bracket_list = {'}':'{',']':'[',')':'('}

  for char in s:
    if char in bracket_list.values():
      stack.append(char)
    elif char in bracket_list:
      if not stack or stack[-1] != bracket_list[char]:
        return False
      stack.pop()
    else:
      return False
    
  return not stack

s1 = "{[()]}"
print("Output:",is_valid(s1)) #TRUE
s2 = "{[(])}"
print("Output:",is_valid(s2)) #FALSE
