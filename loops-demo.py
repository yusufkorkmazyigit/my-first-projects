''''1-100 arasında rastgele üretliecek bir sayıyı 
aşağı ve yukarı ifadeleri ile buldurmaya çalışın
** random modulu için "python random" şeklinde arama yapın
** 100 uzerinden puanlama yapın her soru 20 puan
Hak bilgisini kullanıcıdan alın ve her soru belir-
tilen can sayısı üzeridnen hesaplansın hak=5'''
import random
sayi=random.randint(1,100)
hak=int(input("Hakkınız kaç olsun: "))
sayac = 0

while hak > 0:
    hak -=1
    sayac +=1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler sayıyı {sayac} denemede  bildiniz Toplam puanınız: {100-(100/hak)*(sayac-1)}")
        
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")
    if hak==0:
        print(f"hakkıniz bitti sayi : {sayi}")