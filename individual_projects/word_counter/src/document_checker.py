# BHR 2nd word counter
from helper import *

def view():
  file = txt_reader("docs\\document.txt")
  print(file)
  
def edit():
  file = txt_reader("docs\\document.txt")
  print("Press enter twice to finish")
  view()
  additions = []
  while True:
    addition = input()
    if not addition:
      break
    additions.append(addition)
  updated_file = file + "\n" + "\n".join(additions)
  txt_saver("docs\\document.txt", file)
