def merge_ranges(sessions):
  sorted_sessions = sorted(sessions, key=lambda x:x[0])
  res = []
  for index, element in enumerate(sorted_sessions):
    # If the last element in res already includes this element
    if (len(res) > 0 and res[-1][1] > element[0]):
      continue
    end = find_end(sorted_sessions, index + 1, element)
    if (element == end):
      res.append(element)
    elif end[0] < element[1]:
      res.append(element)
    else:
      res.append((element[0], end[1]))
  return res

def find_end(sessions, index, target):
  # If Sessions
  if (index > len(sessions) - 1):
    return target
  session = sessions[index]
  if target[1] < session[0]:
    return target
  return find_end(sessions, index + 1, session)
  
test_cases = [
  [(0, 1), (4, 8), (3, 5), (10, 12), (9, 10)], 
  [(1, 2), (2, 3)],
  [(1, 5), (2, 3)],
  [(1, 10), (2, 6), (3, 5), (7, 9)]
]
for case in test_cases:
  print(merge_ranges(case))