# BHR 2nd word counter

def view():
  file = txt_reader("docs\\document.txt")
  print(file)
  
def edit():
  file = txt_reader("docs\\document.txt")
  print("Press enter twice to finish")
  view()
  while True:
    addition = input()
    if not addition:
      break
    file.append(addition)
  txt_saver("docs\\document.txt", file)
    
