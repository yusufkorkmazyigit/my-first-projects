''''Girilen Sayının asal olup olmadığını bulalım
Asal sayi 1 ve kendisi hariç tam böleni olmayan sayılardır'''
a=int(input("Sayınızı Giriniz : "))
asalmi=True
if a==1:
    asalmi=False
for i in range(2,a):
    if (a % i == 0):
        asalmi = False
        break

if asalmi:
    print("SAYI ASALDIR")
else:
    print("SAYI ASAL DEGİLDİR")

