soru = int(input('Bir 3 genin mi yoksa 4 genin mi tipini bulmak istiyorsunuz?\n:'))


if soru == 4:
  kenar1 = (int(input('Dortgenin ilk kenar uzunlugunu giriniz: ')))
  kenar2 = (int(input('Dortgenin ikinci kenar uzunlugunu giriniz: ')))
  kenar3 = (int(input('Dortgenin ucuncu kenar uzunlugunu giriniz: ')))
  kenar4 = (int(input('Dortgenin dorduncu kenar uzunlugunu giriniz: ')))
  if (kenar1+kenar2+kenar3+kenar4)%4 == 0:
    print('Bu bir eskenar dortgen!')
  elif (kenar1+kenar2+kenar3+kenar4)%4 != 0:
   print('Bu bir yamuk!')
  if (kenar1+kenar2+kenar3+kenar4)/4 == kenar1:
   print('Bu bir kare!')

elif soru == 3:
  kenar1 = (int(input('Ucgenin ilk kenar uzunlugunu giriniz: ')))
  kenar2 = (int(input('Ucgenin ikinci kenar uzunlugunu giriniz: ')))
  kenar3 = (int(input('Ucgenin ucuncu kenar uzunlugunu giriniz: ')))
  if kenar1 == kenar2 == kenar3:
    print('Bu bir eskenar ucgen!')
  elif kenar1==kenar2:
   print('Bu bir ikizkenar ucgen!')
  elif kenar1 != kenar2 != kenar3:
   print('Bu bir cesitkenar ucgen!')