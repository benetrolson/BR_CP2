#BHR 2nd Personal Library
import csv
#Create the main function from which all the other functions run. 
def main(library):
  while True:
    print("Welcome to your personal library. \nYour options are: \n1. View \n2. Add \n3. Remove \n4. Search \n5. Edit \n6. Exit")
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
      library = edit(library)
    elif check == "6":
      break
    else:
      print("That was not an option. Please try again. ")

#View function
def view(library):
  for i in range(len(library)):
    title = library[i]["Title"]
    author = library[i]["Author"]
    print(f"{i + 1}. {title} by {author}. ")
  if not library:
    print("Your library is empty. ")

#Add function
def add(library):
  title = input("What is the name of the book you want to add? ").strip().title()
  author = input("Who is the author of the book? ").strip().title()
  for book in library:
    if book["Title"] == title and book["Author"] == author:
      print("This book already exists.")
      return library
  library.append({"Title": title, "Author": author})
  print(f"You have added {title} by {author}. ")
  save(library)
  return library

#Remove function
def remove(library):
  while True:
    view(library)
    if not library:
      return library
    removal = input("What is the number of the one you want to remove? ").strip()
    if removal.isdigit():
      removal = int(removal)
      if removal <= len(library) and removal > 0:
        print(f"You removed {library[removal - 1]['Title']} by {library[removal - 1]['Author']}.")
        library.pop(removal - 1)
        save(library)
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
    if not library:
      print("Your library is empty. ")
      return
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
  for i in library:
    if option == "1" and term in i["Title"]:
      print(f"{i['Title']} by {i['Author']}. ")
      found = True
    elif option == "2" and term in i["Author"]:
      print(f"{i['Title']} by {i['Author']}. ")
      found = True
  if not found:
    print("There was no matching item. ")

def edit(library):
  while True:
    view(library)
    option = input("What is the number of the book that you want to edit? ").strip()
    if option <= len(library) and option > 0:
      print("Please try again. That was not included in the options. ")
      continue
    check = input("Do you want to edit \n1. The title \n2. The author \n3. Both \n")
    if check == "1":
      new_title = input("What do you want the title to be changed to? ")
    elif check == "2":
      new_author = input("What do you want the author to be changed to? ")
    elif check == "3":
      new_title = input("What do you want the title to be changed to? ")
      new_author = input("What do you want the author to be changed to? ")
    else:
      print("Please try again. That was not an option. ")
      continue
    if check == "1" or check == "3":
      library[option]["Title"] = new_title
    if check == "2" or check == "3":
      library[option]["Author"] = new_author
    save(library)

def save(library):
  try:
    with open("individual_projects\\personal_library.csv", "w", newline = "") as file:
      fieldnames = ["Title", "Author"]
      writer = csv.DictWriter(file, fieldnames = fieldnames)
      writer.writeheader()
      writer.writerows(library)
  except FileNotFoundError:
    print("The file does not exist. ")
  except Exception as e:
    print(f"A {e} error happened. ")
  return library
  
try:
  with open("individual_projects\\personal_library.csv", "r", newline = "") as file:
    reader = csv.DictReader(file)
    library = list(reader)
except FileNotFoundError:
  library = []
except Exception as e:
  print(f"A {e} error happened. ")

main(library)

