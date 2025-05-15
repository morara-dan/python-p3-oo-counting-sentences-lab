#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False
  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False
  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else:
      return False
    
  def count_sentences(self):
    
    sentences = 0
    l = len(self.value)
    
    for i in range(l):
      char = self.value[i]
      #print(char)
      if char in ['.', '!', '?'] and i + 1 < l and self.value[i + 1] == " ":
        sentences += 1
        print(char)
      elif char in ['.', '!', '?'] and i + 1 == l:
        print(char)
        sentences += 1
    print(sentences)
    return sentences
    



new = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...").count_sentences()