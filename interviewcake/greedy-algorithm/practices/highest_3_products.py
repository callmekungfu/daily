'''
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
'''

def highest_product(list_of_ints):
  if len(list_of_ints) < 3:
    raise ValueError('Less than 3 items!')

  highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
  highest_product = list_of_ints[0] * list_of_ints[1]
  lowest_product = list_of_ints[0] * list_of_ints[1]
  highest = max(list_of_ints[0], list_of_ints[1])
  lowest = min(list_of_ints[0], list_of_ints[1])
  # Walk through items, starting at index 2
  for i in range(2, len(list_of_ints)):
    current = list_of_ints[i]
    highest_product_of_3 = max(highest_product_of_3, current * highest_product, current * lowest_product)
    highest_product = max(highest_product, current * highest, current * lowest)
    lowest_product = min(lowest_product, current * highest, current * lowest)
    highest = max(current, highest)
    lowest = max(current, lowest)
  return highest_product_of_3

