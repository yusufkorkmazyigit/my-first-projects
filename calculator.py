"""
a = float(input("ilk sayıyı giriniz: "))
c = input("istediginiz islem +,-,/,* ")
b = float(input("ilk sayıyı giriniz: "))

if c =="+":
    result = a + b
elif c=="-":
    result = a-b
elif c == "/":
    result = a/b

elif c == "*":
    result=a*b
print(result)
"""

def hesapla(x,y,islem):

    if islem not in "+-*/":
        return("lutfen şu işlemlerden birini seçiniz +-*/")
    if islem == "+":
        return (f"{x} + {y} = " + str(x+y)) 
    if islem == "-":
        return (f"{x} - {y} = " + str(x-y))
    if islem == "*":
        return (f"{x} * {y} = " + str(x*y))
    if islem == "/":
        return (f"{x} / {y} = " + str(x/y))

#while True:
    try:
        x =int(input("ilk sayınız: "))
        y= int(input("ikinci sayınız: "))
        islem=str(input("isleminiz +, -, *, /  =>  "))            
        print(hesapla(x,y,islem))
    except:
        print("Lütfen sayıları düzgün giriniz")
