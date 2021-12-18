sayilar=[1,3,5,7,9,12,19,21]
# 1 sayılar listesindeki hangi sayılar 3 ün katıdır
# for sayi in sayilar:
#    if  (sayi%3==0):
#        print(sayi,"ÜÇÜN KATIDIR")
# # 2 sayılar listesinde sayıların toplamı kaçtır
# toplam=0
# for deger in sayilar:
#     toplam = toplam+deger
# print(toplam)
# # 3  sayilar listesindeki tek sayıların karesini alınız
# for number in sayilar:
#     if number%2==1:
#         kare=number**2
#         print(number,"in karesi",kare)


# sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
# # 4 Sehirlerden hangileri en fazla 5 karakterlidir
# for sehir in sehirler:
#     if len(sehir)> 5:
#         print(sehir)

urunler =[
    {"name":"A1", "price":"3000"},
    {"name":"A2", "price":"4000"},
    {"name":"A3", "price":"5000"},
    {"name":"A4", "price":"6000"},
    {"name":"A5", "price":"7000"}
   
]
# 5- Ürünlerin fiyatlarının toplamı nedir
# toplam=0
# for (urun) in (urunler):
#     toplam=int(urun["price"])+toplam
# print(toplam)
# 6  Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if (int(urun["price"]))<=5000:
        print(urun)
    