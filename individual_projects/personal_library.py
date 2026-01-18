#BHR 2nd Personal Library
library = []

def main(library):
  print("Welcome to your personal library. \nYour options are: \n1. View \n2. Add \n3. Remove \n4 Search \n5. Exit")
  check = input("What do you want to do? ")
  if check == "1":
    view()
  elif check== "2":
    add()
  elif check == "3":
    remove()
  elif check == "4":
    search()
  elif check == "5":
    return "quit"
  else:
    print("That was not an option. Please try again. ")
  return "", library

#View function
def view(library):
  for i in library:
    print(i)

#Add function


#Remove function


#Search function


#Main loop
while True:
  check, library = main(library)
  if check == "quit"
