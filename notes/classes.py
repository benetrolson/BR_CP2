#BHR 2nd Classes
import time as t

#example 1
class Dog:
    def __init__(self, name, breed, age):# Initialize
        self.name = name.capitalize()
        self.breed = breed.title()
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\n"
    
    def speak(self):
        return f"{self.name}: Bark"

doug = Dog("Doug", "Golden Retriever", 3)
pongo = Dog("Pongo", "Dalmation", 8)

#Example 2
class ClassSubject:
    def __init__(self, name, room = None, teacher = "Ms. LaRose"):
        self.name = name.title()
        self.room = room
        self.teacher = teacher
    
    def __str__(self):
        return f"Name: {self.name}\nRoom: {self.room}\nTeacher: {self.teacher}\n"

print(doug)
print(pongo)
while True:
    print(doug.speak())
    t.sleep(1)
    print(doug.speak())
    t.sleep(1)
    print(pongo.speak())
    t.sleep(1)
    print(doug.speak())
    t.sleep(1)
    print(pongo.speak())
    t.sleep(1)
    print(doug.speak())
    t.sleep(1)
    print(doug.speak())
    t.sleep(1)
    print(doug.speak())
    t.sleep(1)
    print(pongo.speak())
    t.sleep(1)
    print(pongo.speak())
    t.sleep(1)
