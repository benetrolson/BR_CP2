# BHR 2nd word counter
from helper import *

def remove_word_count(file_content):
    lines = file_content.splitlines()
    normal_lines = [line for line in lines if not (line.startswith("Word Count:") or line.startswith("Last Updated:"))]
    return "\n".join(normal_lines)

def view():
  file = remove_word_count(txt_reader("docs\\document.txt"))
  print(file)
  
def edit():
  file = remove_word_count(txt_reader("docs\\document.txt"))
  print("Press enter twice to finish")
  view()
  additions = []
  while True:
    addition = input()
    if not addition:
      break
    additions.append(addition)
  word_count = len(updated_content.split())
  timestamp = time_finder()
  word_count_lines = f"\nWord Count: {word_count}\nLast Updated: {timestamp}"
  txt_saver(path, updated_content + word_count_lines)
  updated_file = file + "\n" + "\n".join(additions)
  txt_saver("docs\\document.txt", updated_file)
