# My solution
def merge_lists(a, b):
  res = []
  a_cur = 0
  b_cur = 0
  a_min = a[a_cur]
  b_min = b[b_cur]
  a_done = False
  b_done = False
  for i in range(len(a) + len(b)):
    if (a_min <= b_min or b_done) and (a_cur < len(a)):
      res.append(a_min)
      a_cur += 1
      if (a_cur < len(a)):
        a_min = a[a_cur]
      else:
        a_done = True
    if (a_min >= b_min or a_done) and (b_cur < len(b)):
      res.append(b_min)
      b_cur += 1
      if (a_cur < len(a)):
        b_min = b[b_cur]
      else:
        a_done = True
  return res

# Interview Solution
def merge_lists_sol(my_list, alices_list):
  # Set up our merged_list
  merged_list_size = len(my_list) + len(alices_list)
  merged_list = [None] * merged_list_size

  current_index_alices = 0
  current_index_mine = 0
  current_index_merged = 0
  while current_index_merged < merged_list_size:
    is_my_list_exhausted = current_index_mine >= len(my_list)
    is_alices_list_exhausted = current_index_alices >= len(alices_list)
    if (not is_my_list_exhausted and
            (is_alices_list_exhausted or
              my_list[current_index_mine] < alices_list[current_index_alices])):
        # Case: next comes from my list
        # My list must not be exhausted, and EITHER:
        # 1) Alice's list IS exhausted, or
        # 2) the current element in my list is less
        #    than the current element in Alice's list
        merged_list[current_index_merged] = my_list[current_index_mine]
        current_index_mine += 1
    else:
        # Case: next comes from Alice's list
        merged_list[current_index_merged] = alices_list[current_index_alices]
        current_index_alices += 1

    current_index_merged += 1

  return merged_list

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))