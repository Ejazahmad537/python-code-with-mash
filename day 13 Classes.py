#class is a single word
#for example
# class EmailClient(): #first latter of the word is Capatel

# #another class
# class Point:
#     def move(self):
#         print("Moving...")
#
#     def draw(self):
#         print("Drawing...")
#
# point1 = Point() # we put the object into the veriable
# point1.move()
#
# #Create a program
# #Person
#     #__Name
#     #__talk
# class Person:
#     def talk(self):
#         print("Talking...")
# Ejaz = Person()
# Ejaz.talk()

# #now we make the name attribute
# class Person:
#     def __init__(self, name ):
#         self.name = name
#     def talk(self):
#         print("Talking...")
# Ejaz = Person("Ejaz Ahmad") #this is value in the bricket
# print(Ejaz.name)
# Ejaz.talk()

#........................
#Inheritance of class
#.........................
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):#the dog class will inharat of the matheds define in the mammal class
    pass

class Cat(Mammal): #the car class inherit from mammal class
    pass
dog1 = Dog()
dog1.walk()