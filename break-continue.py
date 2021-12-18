# name="Yusuf KORKMAZYIGIT  "
# for letter in name:
#     if letter ==" ":
#         break
#     print(letter)
# x=0 
# while x< 15 :
#     x+=1
#     if x==10:
#         continue
#     print(x)
#1 - 100 tek sayıların toplamı
x=0
result=0
while x<=99:
    x+=1
    if x%2==0:
        continue
    result=result+x
    print(result)
print(f'toplam = {result}')

