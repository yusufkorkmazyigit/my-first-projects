## BANKAMATIK UYGULAMASI ##
hesapA = {
    "ad": "Yusuf korkmazyiğit",
    "hesapno": "123456",
    "bakiye": 1500,
    "ekhesap": 3800
}
hesapB = {
    "ad": "Memed korkmazyiğit",
    "hesapno": "456123",
    "bakiye": 2500,
    "ekhesap": 6400
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"]>=miktar:
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz.")

    else:
        toplam = hesap["bakiye"]+hesap["ekhesap"]

        if toplam >= miktar:
            ekHesapkullanimi=input("ek hesap kullanılsın mı (e/h)")

            if ekHesapkullanimi == "e":
                bakiye = hesap['bakiye']
                ekhesapkullanılacakmiktar = miktar - bakiye
                hesap ["bakiye"] = 0
                hesap['ekhesap'] = ekhesapkullanılacakmiktar
                print("paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap ['bakiye']} bulunmaktadır")
        else:
            print("üzgünüz bakiye yetersiz")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapno']} hesabınızıda {hesap['bakiye']} TL limitiniz bulunmaktadır ek hesap limitiniz ise {hesap['ekhesap']} .")
paraCek(hesapA,2000)
bakiyeSorgula(hesapA)
paraCek(hesapA,1000)
bakiyeSorgula(hesapA)