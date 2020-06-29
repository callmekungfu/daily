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

# Provided solution
def shuffle_sol(the_list):
    # If it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # Walk through from beginning to end
    for index_we_are_choosing_for in range(0, len(the_list) - 1):

        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index_we_are_choosing_for,
                                         last_index_in_the_list)

        # Place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing_for]

sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)