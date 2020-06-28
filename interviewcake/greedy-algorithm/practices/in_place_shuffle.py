'''
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original 
list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random 
integer that is >= floor and <= ceiling.
'''

import random


def get_random(floor, ceiling):
  return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
  # Shuffle the input in place
  if (len(the_list) <= 1):
    return the_list
  last_index_in_list = len(the_list) - 1
  for i in range(len(the_list) - 1):
    random_choice = get_random(i, last_index_in_list)
    if random_choice != i:
      the_list[i], the_list[random_choice] = the_list[random_choice], the_list[i]


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)