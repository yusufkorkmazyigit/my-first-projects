sayilar=[1,3,5,7,9,12,19,21]
# 1 sayilar lsitesini while ile ekrana yazdırınız
# i=0
# while (i< len(sayilar)):
#     print(sayilar[i])
#     i+=1

# 2 baslangıc ve bitis degerlerini kullanıcıdan alıp
#  aradaki tüm tek sayıları ekrana yazdırınız.
# a=int(input("Başlangıç değerini giriniz: "))
# b=int(input("Bitiş değerini giriniz: "))
# i=a
# while i<b:
#      i+=1
#      if i%2==1:
#         print(i)
    


# 3 1-100 arasındaki sayıları azalan şekilde yazdırın.
# i=100
# while i>0:
#     print(i)
#     i-=1

# 4 Kullanıcıdan alacagınız 5 sayıyı ekrana sırali bir şekilde yazdırınız
# numbers=[]
# i=0
# while i<5:
#     sayi=int(input("sayi: "))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)

# 5 Kullanıcıdan alacagınız sınırsız ürün bilgisini ürünler list saklayın
# ** ürün sayısını kullanıcıya sorun
# ** dictionary listesi yapısı (name,price ) şeklinde olsun
# ** ürün ekleme işlemi bittihine ekrana while ile listeleyiniz 
urunler=[]
a=int(input("kaç ürün gireceksiniz: "))
i=0
while i<a:
    urun=input("urununuzun ismini giriniz: ")
    price=input("urununuzun fiyati: ")
    urunler.append({
        "name":urun,
        "price":price
    })
    i=len(urunler)
print(urunler)
    