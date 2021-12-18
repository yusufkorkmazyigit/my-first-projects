# - 1 - Girilen sayının 0-100 arasında olmasını kontrol ediniz 
# a=float(input("sayınızı giriniz: "))
# if a>0 and a<100:
#     print(a," sayınız 0-100 arasındadır" )
# else:
# #     print(a," sayınız 0-100 aralıgında degildir")
# # - 2 - Gierilen bir sayının pozitif çıft sayı olup olmadıgını kontrol ediniz
# b=float(input("Sayınızı giriniz ;"))
# if b>0 and b%2==0:
#     print(b, " sayınız pozitif aynı zamanda çift sayıdır")
# elif b>0:
#     print("sayınız sıfırdan büyük fakat çift degil")
# elif b%2==0:
# #     print("sayınız çift fakat sıfırdan büyük degil")
# # else: 
# #     print("sayınız ne çift sayı ne de pozitif")

# # # # - 3 - Email ve parola bilgileri ile giriş kontrolu yapınız
# # email="yusufusta@gmail.com"
# # sifre="123"
# # girilenemail=str(input("E- mailinizi giriniz ; "))
# # girilensifre=str(input("Şifrenizi giriniz ; "))
# # if email==girilenemail and sifre==girilensifre:
# #     print("BİLGİLERİNİZ DOGRU HOSGELDİNİZ")
# # else: 
# #     print("YANLIS BILGI GİREMEZSİNZ!")

# # - 4 - Girilen 3 sayıyı büyüklük olarak karşılaştırınız
# z=float(input("İLK SAYINIZI GİRİNİZ "))
# x=float(input("İKİNCİ SAYINIZI GİRİNİZ "))
# y=float(input("ÜÇÜNCÜ SAYINIZI GİRİNİZ "))
# if z>x and z>y: 
#     print("en büyük sayı ilk sayı")
# elif x>y and x>z:
#     print ("en büyük sayı ikinci sayı")
# elif y>x and y>z:
#     print ("en büyük sayı 3. sayıdır")
# else:
#     print("sayılarda eşitlik vardır!")


# - 5 - Kullanıcıdan 2 bize (%60)ve final (%40) notunu alıp ortalama hesaplayınız
#        eğer ortalama 50 ve üstünde ise geçti degilse kaldı yazdırınız 
#           a) ortalama 50 olsa bile final notu en az 50 olmalıdır
#           b) finalden 70 alan tartışmasız geçsin
vize1=float(input("İlk vizenizi giriniz: "))
vize2=float(input("İkinci vizenizi giriniz: "))
final=float(input("Finalinizi giriniz: "))
ortalama=(((vize1+vize2)/2)*(6/10))+(final*(4/10))
print("ORTALAMANIZ; ",ortalama)
if final>=70:
    print("Geçtiniz! ")
elif ortalama>=50 and final>=50:
    print("Geçtiniz!")
else:
    print("Kaldınız!")
