# # key - value şeklinde çalışır
# # 41 => Kocaeli, 38 => Kayseri

# sehirler=["yozgat","kayseri"]
# plakalar=[66,38]

# # print(plakalar[sehirler.index("kayseri")])

# #print(plakalar["yozgat"]) => 66

# plakalar= {"yozgat":66, "kayseri":38,"konya":42}
# print(plakalar["yozgat"])
# plakalar["ankara"]=6
# print(plakalar)

users={
"yusuf":{
    "age": 19,
    "roles": ["user"],
    "email":"yusuf.korkmazyigit@gmail.com",
    "adres": "Kayseri/kocasinan",
    "telefon": "54654465"
},
"ataturk":{
    "age": 140,
    "roles":["admin","user"],
    "email": "ataturk@gmail.com",
    "adres": "selanik",
    "telefon": "13213152", 
}
}
print(users["ataturk"]["roles"][0])
#ataturk kullanıcısın rollerinden 0 ıncısını yazdır