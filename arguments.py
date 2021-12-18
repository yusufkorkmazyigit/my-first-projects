 def changeName(n):
     n = "Yusuf"

name = "Memed"
changeName(name)
print(name)

def change(n):
     n[0]= "Istanbul"

sehirler =["Ankara", "İzmir"]
n = sehirler [:]
change(sehirler)
print(sehirler)

 def add(*params):
     sum=0
     for n in params:
         sum = sum+n
     return sum

 print(add(10,20,30,50,60))
 def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print("{} is {}".format(key,value))
displayUser (name="Yusuf",age=19,city="Kayseri")
displayUser (name="Tahir",age=91,city="Yozgat",phone=123456)

