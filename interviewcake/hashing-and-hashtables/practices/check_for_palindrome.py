# My solution
# O(n)
def is_palindrome(word):
  char_map = {}
  # Build Map
  for char in word:
    char_map[char] = char_map[char] + 1 if char in char_map else 1
  if (len(word) % 2 == 1):
    # Odd number of characters
    found_odd = False
    for key in char_map:
      occurance = char_map[key]
      if found_odd and occurance % 2 == 1:
        return False
      if occurance % 2 == 1:
        found_odd = True
  else:
    # Even number of characters
    for key in char_map:
      occurance = char_map[key]
      if occurance % 2 == 1:
        return False
  return True

# Given Solution
# O(n)
def has_palindrome_permutation(the_string):
  # Track characters we've seen an odd number of times
  unpaired_characters = set()

  for char in the_string:
    if char in unpaired_characters:
      unpaired_characters.remove(char)
    else:
      unpaired_characters.add(char)

  # The string has a palindrome permutation if it
  # has one or zero characters without a pair
  return len(unpaired_characters) <= 1
print(is_palindrome('ivicc'))