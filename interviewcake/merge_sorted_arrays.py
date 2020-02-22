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

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))