# #kullanıcıdan isim, yaş ve egeitim bilgilerini isteyip ehliyet
# # alabilme durumunu kontrole diniz. Ehliyet alma şartı minimum 18 yaş ve 
# # # lise yada ünviersite mezunu olunmasıdır.
# isim=input("isminizi giriniz : ")
# yas=int(input("yasınızı giriniz :  "))
# egitim=(input("egitimin durumunuzu girinniz(lise veya universite yazınız ):  "))
# if yas>=18:
#     if(egitim=="lise"or egitim=="universite"):
#      print(isim, " ehliyet alabilirsin")
#     else:
#         print(isim, " ehliyet alamlazsın egitim durumun yetersinz")
# else:
#     print(isim, " ehliyet alamasınz yaşın tutmuyor")
# # Bir ögrencinin 2 yazılı bir sözlü notunu alığ hesaplanan
# ortalamaya göre not aralgıgına karşılık gelen not bilgisini yazdırınız
# 0-24 0
# 25-44 1
# 45-54 2
# 55-69 3
# 70-84 4
# # 85-100 5
# from types import LambdaType
# from typing import List


# sınav1=float(input("ilk sınavınızı giriniz : "))
# sınav2=float(input("ikinci sinavınızı giriniz: "))
# sozlu=float(input("sözlü notunuzu girinizi: "))
# sonuc=float((sınav1+sınav2+sozlu)/3)
# print ("ortalamanız ", sonuc)
# if sonuc<25:
#     print("0")
# elif sonuc<45:
#     print("1")
# elif sonuc<55:
#     print("2")
# elif sonuc<70:
#     print("3")
# elif sonuc<85:
#     print("4")
# else:
#     print("5")
# # Trafige çıkış tarihi alınan bir aracın servis zamanını hesaplayınız
# # 1. bakım  1, yıl
# # # 2. bakım  2, yıl
# # 3. bakım 3, yıl 
# # **Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesapla
# # **datetime modulunu kullanmamız gerekli
# (simdi)-(2021/11/25) => Gün
import datetime

tarih=str(input("aracınız habngi tarihte trafige çıktı: (20xx/x/x) "))
tarih= tarih.split("/")
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])
trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi= datetime.datetime.now()
fark=simdi - trafigecikis
days=(fark.days)

if days<=365:
    print("1. servis aralığı")
elif days> 365 and days<=365*2:
    print("2. servis aralığı")
elif days>365*2 and days<=365*3:
    print("3. servis aralığı")
else:
    print("hatalı süre bilgisi ")