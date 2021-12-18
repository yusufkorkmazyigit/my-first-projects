# def carpma_yap(x,y):
#     print(x*y)

# carpma_yap(3,5)

# #ön tanımlı argüman.

# def carpma_yap(x,y=1):
#     print(x*y)
# carpma_yap(4)
# def carpma_yap(x,y=1):
#     print(x*y)
# carpma_yap(4,6)

# carpma_yap(x=8,y=7)
 

 # direk yazar 
# def direk_hesap(isi,nem,sarj):
#     print((isi+nem)/sarj)

# cikti=direk_hesap(25,40,70)
# print(cikti)

 # çıktıyı baska bir fonsiyonun girdisi olarak kullanmak için
def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

print(direk_hesap(30,40,60))