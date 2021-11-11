# I girilen 2 sayıdan hangisi büyüktür
 # a=input("1. sayıyı giriniz: ")
 # b=input("2. sayıyı giriniz: ")
 # print("cevap true ise ilk sayı büyük false ise ikinci sayı büyük")
 # sonuc=a>b
 # print(sonuc)
#  II #kullanıcıdan 2 vize %60 ve final %40 alıp ort hesaplayınız
# vize1=float(input("ilk vizenizi giriniz: "))
# vize2=float(input("ikinci vizenizi giriniz: "))
# final1=float(input("final sınavınızı giriniz: "))
# vizeort=(vize1+vize2)/2
# vizeetkisi=vizeort*6/10
# finaletkisi=final1*4/10
# puan=vizeetkisi+finaletkisi
# # eğer ortalama 50 ve üstünde ise geçti degilse kaldı yazdırınız
# print("puanınız: ",puan)
# if puan>=50:
#  print(puan,"puan ile geçtiniz")
# else:
#  print(puan,"puan ile kaldınız")
# III girilen sayının tek mi çift mi oldugunu yazdırınız
# print("tek çift belirleyici ")

# a=float(input("sayıyı giriniz: "))
# if a%2==1:
#     print("sayı tektir")
# else:
#     print("sayı çifttir")
# # IV Girilne bir sayının negatıf mi pozitif mi oldugunuz yazdırınız
# print("sayının pozitif veya negatif oldugunu belirteç piyasalarda")
# x=float(input("sayınızı yazınız: "))
# if x==0:
# #     print ("sayınız sıfırdır")
# # elif x>0:
# #     print("sayınız pozitiftir")
# # else:
# #     print("sayınız negatiftir")
# # # V Paralo ve email bilgisini isteyim dogrulugunun kontrol ediniz
# # ;(email=email@yusufusta.com parola=abc123)
email,parola="email@yusufusta.com","abc123"
a=str(input("emailinizi giriniz => "))
b=str(input("parolanızı giriniz => "))
emaildogruluk= a==email
paroladogruluk= b==parola
print("emailiniz",emaildogruluk,"*** " "şifreniz",paroladogruluk)