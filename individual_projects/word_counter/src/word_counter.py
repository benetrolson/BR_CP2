# BHR 2nd word counter
from helper import *

def word_counter():
  word_count = 0
  document = txt_reader("docs\\document.txt")
  if document is None:
    return 0
  word_count = document.split()
  return len(word_count)
