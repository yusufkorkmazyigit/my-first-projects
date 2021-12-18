def sayHello(name = "user"):
    return("Hello  "+ name)
msg=sayHello("Yusuf")
msg=sayHello("Tahir")

print(msg)

def total(num1, num2):
    return num1+num2

result = total(10,20)
print(result)

def yasHesapla(dogumyili):
    '''
    DOCSTRING : doğum yılınıza göre emekliligine kaç yıl kaldı
    INPUT : Dogum Yılı
     OUTPUT: Hesaplanan yıl bilgisi
    '''
    return 2021- dogumyili
ageYusuf = yasHesapla(2002)
print(ageYusuf)

def EmekliligeKalan (dogumyili,isim):
    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emekliliginize {emeklilik} yıl kaldı")
    else:
        print("Emeklisiniz")

EmekliligeKalan(2002,"Yusuf")

list=[1,2,3]
print(help(list.append))