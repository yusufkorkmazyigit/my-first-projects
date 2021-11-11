x, y, z=5,10,7
# print(x,y,z)
# x,y=y,x
# # print(x,y,z)
# # !!! SAĞDAKİ İŞLEMLER SOL TARAFA ATANIR !!!
# x+=5 #x = x + 5 e karşılık gelir
# x-=5 #x = x - 5 e karşılık gelir
# x*=5 #x = x * 5 e karşılık gelir
# x/=5 #x= x / 5 e karşılık gelir.
# x%=5 # x in 5 e bölümünden kalanı x e atar""
# z//=2 #z i 2 e böler ve bölümün tam kısmını z ye atar.
# y**= 3 # y üssü 3 ü y ye verir
# y*=z  #  y = y*z
# #print(x,y,z)

values=1,2,3,4,5
print(values)
print(type(values))
x, y, *z = values

print(x,y,z)
print(z)
print(z[1])