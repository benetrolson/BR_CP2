# BHR 2nd word counter
from helper import *
from time_finder import time_finder
from word_counter import word_counter

def remove_word_count(file_content):
    lines = file_content.splitlines()
    normal_lines = [line for line in lines if not (line.startswith("Word Count:") or line.startswith("Last Updated:"))]
    return "\n".join(normal_lines)

def view(path):
  file = remove_word_count(txt_reader(path))
  print(file)
  
def edit(path):
  file = remove_word_count(txt_reader(path))
  print("Press enter twice to finish")
  view(path)
  additions = []
  while True:
    addition = input()
    if not addition:
      break
    additions.append(addition)
  updated_content = file
  if additions:
    updated_content += "\n" + "\n".join(additions)
  word_count = word_counter(updated_content)
  timestamp = time_finder()
  word_count_lines = f"\nWord Count: {word_count}\nLast Updated: {timestamp}"
  txt_saver(path, updated_content + word_count_lines)
