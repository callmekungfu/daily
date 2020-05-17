'''
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. 
So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that 
their rankings aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

- a list of unsorted_scores
- the highest_possible_score in the game and returns a sorted list of scores in less than O(nlgn) time.
'''

def sort_scores(unsorted, highest_possible):
  score_map = {}
  sorted_scores = []
  for num in unsorted:
    if (num in score_map):
      score_map[num] = score_map[num] + 1
    else:
      score_map[num] = 1
  for score in range(highest_possible, -1, -1):
    if (score in score_map):
      filler = [score for i in range(score_map[score])]
      sorted_scores = sorted_scores + filler
  return sorted_scores

# Given solution
def sort_scores_sol(unsorted_scores, highest_possible_score):
  # List of 0s at indices 0..highest_possible_score
  score_counts = [0] * (highest_possible_score+1)

  # Populate score_counts
  for score in unsorted_scores:
      score_counts[score] += 1

  # Populate the final sorted list
  sorted_scores = []

  # For each item in score_counts
  for score in range(len(score_counts) - 1, -1, -1):
      count = score_counts[score]

      # For the number of times the item occurs
      for time in range(count):
          # Add it to the sorted list
          sorted_scores.append(score)

  return sorted_scores

print(sort_scores([89, 89, 41, 65, 91, 53], 100))
  