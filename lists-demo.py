cars=["Bmw","Mercedes","Opel","Mazda"]#liste
print(len(cars))#uzunluk
print(cars[-1])#son eleman
cars[-1]="Toyota"#son elemanı toyota yapar
sonuc ="Mercedes" in cars #cars ta mercedes var mı?
sondaniki=(cars[-2]) #sondan ikinci 
ilkuc=(cars[0:3])#ilk uc indeks
cars[-2:]=["Toyota","Renault"]
cars=cars+["audi","nissan"]
del cars[-1]#son elemanı sildi
cars=cars[::-1]#terse döndü
studentA=["yiğit","bilgi",2010,[70,60,70]]
studentB=["sena","turan",[80,80,70]]


result=studentA[0]
result=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yasında ve not ortalamsı {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"



print(result)
print(cars)
print(ilkuc)
print(sondaniki)
print(sonuc)