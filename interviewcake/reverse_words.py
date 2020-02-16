# new copy
def reverse_words(message):
  # Reverse entire message
  reverse(message, 0, len(message) - 1)
  last_index = 0
  for i, char in enumerate(message):
    if char == ' ':
      reverse(message, last_index, i - 1)
      last_index = i + 1
  reverse(message, last_index, len(message) - 1)
  print(''.join(message))


def reverse(list_of_chars, start, end):
  left_index  = start
  right_index = end

  while left_index < right_index:
    # Swap characters
    list_of_chars[left_index], list_of_chars[right_index] = \
        list_of_chars[right_index], list_of_chars[left_index]
    # Move towards middle
    left_index  += 1
    right_index -= 1

def split(word): 
  return [char for char in word]  

reverse_words(split('everybody world hello'))