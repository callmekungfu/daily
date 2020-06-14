'''
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
'''

import random


def get_random(floor, ceiling):
  return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
  # Shuffle the input in place


  pass


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)