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

print(reverse_str_in_place(['h', 'e', 'l', 'l', 'o']))