# inheritance ( Kalıtım) : miras alma

# Person = name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(), Cat()

class Person():
    def  __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print("Person Created")

    def who_am_i(self):
        print("ı am a person")

    def eat(self):
        print("i am eating")


class Student(Person):
    def __init__(self,name,surname,number):
        Person.__init__(self,name,surname)
        self.studentNumber = number
        print("Student Created")
    #override;
    def who_am_i(self):
            print("i am a student")
    
    def sayHello(self):
        print("Hello ı am a Student")


class Teacher(Person):
    def __init__(self,name,surname,branch):
        super().__init__(name,surname)
        self.branch=branch
    def who_am_i(self):
        print(f"i am a {self.branch} teacher")


p1 = Person("ali","memiş")
s1 = Student("aynalı","tahir",562)
t1 = Teacher("Alpaslan","Güngor","physic")

print(p1.name + " " + p1.surname)
print(s1.name + " " + s1.surname+ " "+ str(s1.studentNumber))
t1.who_am_i()
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()

