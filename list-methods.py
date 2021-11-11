numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b']

val=min(numbers)
val=max(numbers)
val=max(letters)

val=numbers[2:7]
val=numbers[:4]
val=letters[1:3] 
numbers[5]=40  # 5 elemanı kırk yaptık
numbers.append(81) #sona 81 ekledik
numbers.insert(3,61) #3. eleman 61 olacak şekilde 61 sokar
numbers.insert(-1,69) 
numbers.pop(0) # 0 ıncı eleman sılınır
numbers.remove(5) # isimi 5 olan eleman silinir
numbers.sort() #sıralar
letters.sort() #alfabetik sıralar
numbers.reverse() # büyükten küçüğe sıralar

print(len(numbers)) # kaç elemanlı
print(len(letters)) # kaç elemanlı 
print(numbers.count(10)) #kaç tane 10 var

numbers.clear()#elemanları siler
print(numbers)
print(letters)