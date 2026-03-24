# Class Relationships
#Composition (In a)

class Engine:
    def __init__(self, model):
        self.cyliders = model
    def __str__(self):
        return self.cyliders
    
# Inheritance (Is a)

#Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Vroom! ")

#child car
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.engine = Engine("v8")

class Boat(Vehicle):
    def move(self):
        print("Sail! ")

class Plane(Vehicle):
    def move(self):
        print("Fly! ")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()

#Aggregate (Has a)

class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    def add_book(self, book):
        self.catalog.append(book)
    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("That book doesn't exist. ")
    def view_catalog(self):
        for book in self.catalog:
            print(book)
    def title(self):
        return f"{self.name}"

class Book:
    def __init__(self, title, author, library = "Bennett's bookshelf"):
        self.title = title
        self.author = author
        self.library = library
    def __str__(self):
        return f"{self.title} by {self.author} from the {self.library}"

lib = Library("Provo Library")
book = Book("Inkheart", "Cornelia Funke")
print(book)
lib.add_book(Book("The Way of Kings", "Brandon Sanderson", lib.title()))
lib.add_book(Book("The Fellowship of the Ring", "J. R. R. Tolkien", lib.title()))
lib.add_book(Book("The Last Battle", "C. S. Lewis", lib.title()))
lib.add_book(Book("The Great Hunt", "Robert Jordan", lib.title()))
lib.view_catalog()








