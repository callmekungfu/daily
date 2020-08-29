import string

'''
You want to build a word cloud, an infographic where the size of a word 
corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and 
builds its word cloud data in a dictionary, where the keys are words
and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

> 'After beating the eggs, Dana read the next step:'
> 'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, 
your final dictionary should include one "Add" or "add" with a value of 
22. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
'''

def make_word_map(message):
  cleaned = split_words(message)
  word_map = {}
  for word in cleaned:
    word = word.lower()
    if word in word_map:
      word_map[word] += 1
    else:
      word_map[word] = 1
  print(word_map)

def split_words(message):
  words = []
  word_i = 0
  word_length = 0
  for i, char in enumerate(message):
    if char.isalpha():
      if word_length == 0:
        word_i = i
      word_length += 1
    else:
      word = message[word_i:word_i + word_length]
      words.append(word)
      word_length = 0
  return words

make_word_map("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.")