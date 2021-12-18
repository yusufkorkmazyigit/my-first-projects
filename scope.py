#global scope
"""
x = "global x"


def function():
    #local scope
     #x = "local x"
     print(x)


function()

print(x)

"""
##########################################
"""
#global
name="Yusuf"

def changeName (new_name):
    #local
    name = new_name
    print(name)
changeName("Ada")

print(name)
"""
##########################################
"""
name = "Global String"

def greeting():
    #name="Cınar"
    def hello():
        print("hello "+ name)

    hello()

greeting()
"""
###########################################
'''
x=50
def test(x):
    print(f"x : {x}")

    x =100
    print((f"change x to {x}"))

test(x)
print(x)
'''
#Global olarak güncelleme için 
x=50
def test():
    global x 
    print(f"x : {x}")

    x =100
    print((f"change x to {x}"))

test()
print(x)