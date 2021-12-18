#class
class Person:
    #class attributes
    address = "no information"

    #constructor (yapıcı metod)
    def __init__(self,name,year):

            #object attributes
            self.name = name
            self.year = year
            print("init metodu calıstı.")

    #methods
    def intro(self):
        print("Hello There.I am "+self.name)

#object (instance)

p1 = Person("Yusuf",2002)
#print(p1)

#instance methods:

p1.intro()

#updating
p1.name="Tahir"

#accesing object attributes
#print(f"name: {p1.name} year: {p1.year} address:{p1.address}")

# print(type(p1))

