#1 Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon
'''
def yazdir(kelime,adet):
    print(kelime*adet)

yazdir("yusuf\n",5)
'''

#2 Kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonk.
'''
def listeyeCevir(*degerler):
    liste=[]
    for deger in degerler:
        liste.append(deger)

    return liste

result = listeyeCevir(10,20,30,"Hello")

print(result)
'''
#3 Gönderlilen 2 sayı arasındaki tüm asal sayıları bulunuz.
'''
sayi1 = int(input("sayı 1 : "))
sayi2 = int(input("sayı 2 : "))

def asalSayiBul (sayi1,sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

asalSayiBul(sayi1,sayi2)
'''

#4 Gönderilen bir sayının tam bölenlerini liste şekilde döndür.

def tamBolenbul(sayi):
    tamBolenler=[]

    for i in range (2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

a = int(input("hangi sayının tam bölenleri : "))
print(tamBolenbul(a))