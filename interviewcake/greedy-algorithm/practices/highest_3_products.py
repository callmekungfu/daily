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

# Given Solution
def highest_product_of_3(list_of_ints):

  if len(list_of_ints) < 3:
      raise ValueError('Less than 3 items!')

  # We're going to start at the 3rd item (at index 2)
  # so pre-populate highests and lowests based on the first 2 items.
  # We could also start these as None and check below if they're set
  # but this is arguably cleaner
  highest = max(list_of_ints[0], list_of_ints[1])
  lowest  = min(list_of_ints[0], list_of_ints[1])
  highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
  lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

  # Except this one--we pre-populate it for the first *3* items.
  # This means in our first pass it'll check against itself, which is fine.
  highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

  # Walk through items, starting at index 2
  for i in range(2, len(list_of_ints)):
      current = list_of_ints[i]

      # Do we have a new highest product of 3?
      # It's either the current highest,
      # or the current times the highest product of two
      # or the current times the lowest product of two
      highest_product_of_3 = max(highest_product_of_3,
                                  current * highest_product_of_2,
                                  current * lowest_product_of_2)

      # Do we have a new highest product of two?
      highest_product_of_2 = max(highest_product_of_2,
                                  current * highest,
                                  current * lowest)

      # Do we have a new lowest product of two?
      lowest_product_of_2 = min(lowest_product_of_2,
                                current * highest,
                                current * lowest)

      # Do we have a new highest?
      highest = max(highest, current)

      # Do we have a new lowest?
      lowest = min(lowest, current)

  return highest_product_of_3