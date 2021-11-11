from typing import no_type_check_decorator


website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama"
sonuc=" merhaba dunya "
# boşlukları sildik # sonuc=sonuc.strip()
sonuc=sonuc.rstrip() #sagdan sildik
sonuc= "www.sadikturan.com".strip("w.moc")
sonuc=course.lower()
sonuc=course.upper()
sonuc=course.title()
sonuc=website.count("w")#kaç tane var
sonuc=website.startswith("http")
sonuc=website.endswith("moc")
sonuc = website.find("com")
sonuc=course.isalpha()
sonuc= "hello".isalpha()#hello alfabetik karakterlerden mi oluşuyor true or false
sonuc="123".isdigit()# "123" ifadesi numerik karakterlerden mi oluşuyor ture or false
sonuc="contents".center(50,"-")
sonuc="contents".ljust(50,"-")
sonuc="contents".rjust(50,"-")#sağa yaslar 50 karakter olsturup ikinci degiskenle doldurur
sonuc=course.replace(" ","_")#(coursedaki "boşluk"ları "_" yaptık)
sonuc=course.replace(" ","")# " " ==> ""
sonuc="hello world".replace("world","there")#world ==> there
sonuc=course.split(" ")#boşluklardan ayırır
sonuc=sonuc[2]










print(sonuc)