sayi = int(input("Faktöriyelini hesaplamak istediginiz sayıyı giriniz: "))
sonuc = 1
while sayi > 0:
    sonuc = sonuc * sayi
    sayi -= 1
print(sonuc)
