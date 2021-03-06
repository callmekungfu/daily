'''
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, 
but they complain that the plane usually lands before they can see the ending. 
So you're building a feature for choosing two movies whose total runtimes will 
equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of 
integers movie_lengths (in minutes) and returns a boolean indicating whether there
are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

- Assume your users will watch exactly two movies
- Don't make your users watch the same movie twice
- Optimize for runtime over memory
'''

# My solution
# Build a dictionary by iterating through the array
# Then check every element in the list until one satisfies the requirements
# We can do this in O(n) time, where n is the length of movie_lengths.
def has_two_movies_with_good_runtime(flight_length, movie_lengths):
  movie_map = {}
  # Build Map
  for length in movie_lengths:
    movie_map[length] = movie_map[length] + 1 if length in movie_map else 1
  # Check for valid cases
  for movie in movie_lengths:
    minutes_needed = flight_length - movie
    if (minutes_needed <= 0) or ((minutes_needed in movie_map) and (minutes_needed != movie or movie_map[movie] > 1)):
      return True
  return False

# Interview cake solution
def can_two_movies_fill_flight(movie_lengths, flight_length):
  # Movie lengths we've seen so far
  movie_lengths_seen = set()

  for first_movie_length in movie_lengths:
    matching_second_movie_length = flight_length - first_movie_length
    if matching_second_movie_length in movie_lengths_seen:
      return True
    movie_lengths_seen.add(first_movie_length)

  # We never found a match, so return False
  return False
print(has_two_movies_with_good_runtime(40, [20, 20, 40]))