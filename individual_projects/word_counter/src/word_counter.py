# BHR 2nd word counter

def word_counter():
  word_count = 0
  document = txt_reader("docs\\document.txt")
  for " " in document:
    word_count += 1
  return word_count
    
