#BHR 2nd Personal Library
library = [
  ("The Hobbit", "J.R.R Tolkien"),
  ("A Wrinkle in Time", "Madeleine L'Engle"),
  ("Steelheart", "Brandon Sanderson"),
  ("The Chronicles of Narnia: The Horse and His Boy", "C.S. Lewis"),
  ("The Giver", "Lois Lowry"),
  ("Howl's Moving Castle", "Diana Wynne Jones"),
  ("Artemis Fowl", "Eoin Colfer"),
  ("Fablehaven", "Brandon Mull"),
  ("Inkheart", "Cornelia Funke")]

#Create the main function from which all the other functions run. 
def main(library):
  print("Welcome to your personal library. \nYour options are: \n1. View \n2. Add \n3. Remove \n4. Search \n5. Exit")
  check = input("What do you want to do? ").strip()
  if check == "1":
    view(library)
  elif check== "2":
    library = add(library)
  elif check == "3":
    library = remove(library)
  elif check == "4":
    search(library)
  elif check == "5":
    return "quit", library
  else:
    print("That was not an option. Please try again. ")
  return "", library

#View function
def view(library):
  for i in range(len(library)):
    title, author = library[i]
    print(f"{i + 1}. {title} by {author}. ")

#Add function
def add(library):
  title = input("What is the name of the book you want to add? ").strip().title()
  author = input("Who is the author of the book? ").strip().title()
  library.append((title, author))
  print(f"You have added {title} by {author}. ")
  return library

#Remove function
def remove(library):
  while True:
    removal = input("What is the number of the one you want to remove? ").strip()
    if removal.isdigit():
      removal = int(removal)
      if removal <= len(library) and removal > 0:
        library.remove(library[removal - 1])
        return library
      elif removal <= 0:
        print("Your number is too small. Please try again. ")
      else:
        print("Your number is too big. Please try again. ")
    else:
      print("That is not a number. Please try again. ")

#Search function
def search(library):
  found = False
  while True:
    option = input("Do you want to search by: \n1. Title \n2. Author \n").strip()
    if option == "1":
      term = input("What is the name of the book? ").title().strip()
      break
    elif option == "2":
      term = input("What is the author's name? ").title().strip()
      break
    else:
      print("That is not a valid option. Please try again? ")
      continue
  for title, author in library:
    if option == "1" and term in title:
      print(f"{title} by {author}. ")
      found = True
    elif option == "2" and term in author:
      print(f"{title} by {author}. ")
      found = True
  if found == False:
    print("There was no matching item. ")

#Main loop
while True:
  check, library = main(library)
  if check == "quit":
    break
