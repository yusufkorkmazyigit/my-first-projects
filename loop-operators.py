# **range methodu** = baslangıç,bitiş,artış miktarı
# for item in range(50,100,10): 
#     print(item)
# print(list(range(50,100,10)))

# **enumerate**
# index=0
# greeting="Hello There"
# for letter in enumerate(greeting):
#     print(letter)

# **zip** index numaralarına göre liste birleştir
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))


for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,c)

