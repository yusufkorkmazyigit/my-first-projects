#normal yol
x=6
hak= 5 
devam= "e"
result = 5<=x<10
#and ve kapısı 
result = (x>5) and (x<10)
result=(hak>0)and(devam=="e")
#or
result=(x>8)or(x%2==0)


#not
result=not(x>0)

#x 5 ile 10 arasında olan bir çift sayı mı ?
cevap=(x>5)and(x<10)and(x%2==0)

print(result)
print(cevap)