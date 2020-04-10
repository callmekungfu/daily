# My Solution
# O(n/2)
def reverse_str_in_place(str_list):
  left = 0
  right = len(str_list) - 1
  if (len(str_list) <= 1):
    return str_list
  for i in range(len(str_list) // 2):
    temp = str_list[right]
    str_list[right] = str_list[left]
    str_list[left] = temp
    left += 1
    right -= 1
  return str_list

# Interview Cake Solution
def reverse(list_of_chars):
  left_index  = 0
  right_index = len(list_of_chars) - 1

  while left_index < right_index:
      # Swap characters
      list_of_chars[left_index], list_of_chars[right_index] = \
          list_of_chars[right_index], list_of_chars[left_index]
      # Move towards middle
      left_index  += 1
      right_index -= 1

# Test Code
print(reverse_str_in_place(['h', 'e', 'l', 'l', 'o']))